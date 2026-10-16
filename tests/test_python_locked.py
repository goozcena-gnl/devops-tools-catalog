import os
import shlex
import shutil
import subprocess
from copy import deepcopy
from types import SimpleNamespace

import pytest
import yaml

import scripts.python_constraints as constraints


def distribution(name, version="1.0", requires=(), requires_python=">=3.11"):
    return SimpleNamespace(
        metadata={"Name": name, "Requires-Python": requires_python},
        version=version,
        requires=list(requires),
    )


@pytest.fixture
def locked():
    pins = dict.fromkeys(["hatchling", "editables", "demo", "transitive"], "1.0")
    installed = [
        distribution("hatchling"),
        distribution("editables"),
        distribution("demo", requires=["transitive>=1,<2"]),
        distribution("transitive"),
        distribution("pip", "99.0"),
        distribution("devops-tools-catalog", "0.5.0"),
    ]
    project = {
        "build-system": {"requires": ["hatchling>=1,<2"]},
        "project": {
            "requires-python": ">=3.11",
            "dependencies": ["demo>=1,<3"],
            "optional-dependencies": {"dev": []},
        },
    }
    return pins, installed, project


def test_valid_locked_environment(locked):
    constraints.validate_locked(*locked)


@pytest.mark.parametrize(
    "line",
    [
        "demo>=1.0",
        "demo===1.0",
        "demo==",
        "==1.0",
        "-demo==1.0",
        "demo==1.*",
        "demo[extra]==1.0",
        "demo==1.0; python_version>'3'",
        "demo @ https://example.org/demo.whl",
        "demo==1.0 # comment",
    ],
)
def test_malformed_pin_syntax(line):
    with pytest.raises(ValueError, match="expected pinned"):
        constraints.parse_pinned_requirements([line])


@pytest.mark.parametrize("second", ["demo_pkg==1.0", "DEMO.PKG==2.0"])
def test_duplicate_and_inconsistent_pins(second):
    with pytest.raises(ValueError, match="duplicate pin"):
        constraints.parse_pinned_requirements(["demo-pkg==1.0", second])


def test_invalid_pep440_version(locked):
    pins, installed, project = locked
    pins["demo"] = "1..0"
    with pytest.raises(ValueError, match="Invalid version"):
        constraints.validate_locked(pins, installed, project)


def test_empty_pins_fail(locked):
    with pytest.raises(ValueError, match="no relevant pins"):
        constraints.validate_locked({}, locked[1], locked[2])


def test_missing_transitive_dependency_even_when_absent_from_both_sets(locked):
    pins, installed, project = locked
    del pins["transitive"]
    installed = [d for d in installed if d.metadata["Name"] != "transitive"]
    with pytest.raises(ValueError, match="missing dependency: transitive"):
        constraints.validate_locked(pins, installed, project)


def test_missing_transitive_pin_with_dependency_installed(locked):
    pins, installed, project = locked
    del pins["transitive"]
    with pytest.raises(ValueError, match="unexpected=.*transitive"):
        constraints.validate_locked(pins, installed, project)


def test_wrong_installed_version(locked):
    pins, installed, project = locked
    installed[2].version = "1.1"
    with pytest.raises(ValueError, match="wrong_version=.*demo"):
        constraints.validate_locked(pins, installed, project)


def test_missing_installed_pin(locked):
    pins, installed, project = locked
    with pytest.raises(ValueError, match="missing=.*demo"):
        constraints.validate_locked(pins, installed[0:2] + installed[3:], project)


def test_unexpected_installed_package(locked):
    pins, installed, project = locked
    installed.append(distribution("unrelated"))
    with pytest.raises(ValueError, match="unexpected=.*unrelated"):
        constraints.validate_locked(pins, installed, project)


def test_unused_pin_is_not_accepted_even_if_installed(locked):
    pins, installed, project = locked
    pins["unrelated"] = "1.0"
    installed.append(distribution("unrelated"))
    with pytest.raises(ValueError, match="outside the declared dependency closure"):
        constraints.validate_locked(pins, installed, project)


def test_duplicate_installed_distributions_fail(locked):
    pins, installed, project = locked
    installed.append(distribution("DEMO"))
    with pytest.raises(ValueError, match="duplicate installed distribution"):
        constraints.validate_locked(pins, installed, project)


@pytest.mark.parametrize("scope", ["runtime", "dev", "build", "transitive"])
def test_broken_dependency_declaration(locked, scope):
    pins, installed, project = locked
    if scope == "runtime":
        project["project"]["dependencies"] = ["demo>=2"]
    elif scope == "dev":
        project["project"]["optional-dependencies"]["dev"] = ["demo>=2"]
    elif scope == "build":
        project["build-system"]["requires"] = ["hatchling>=2"]
    else:
        installed[2].requires = ["transitive>=2"]
    with pytest.raises(ValueError, match="incompatible"):
        constraints.validate_locked(pins, installed, project)


def test_invalid_requirement_declaration(locked):
    pins, installed, project = locked
    project["project"]["dependencies"] = ["demo >=> broken"]
    with pytest.raises(ValueError):
        constraints.validate_locked(pins, installed, project)


@pytest.mark.parametrize("scope", ["project", "distribution"])
def test_python_version_requirements_are_checked(locked, scope):
    pins, installed, project = locked
    if scope == "project":
        project["project"]["requires-python"] = ">=99"
    else:
        installed[2].metadata["Requires-Python"] = ">=99"
    with pytest.raises(ValueError, match="Python"):
        constraints.validate_locked(pins, installed, project)


def test_markers_extras_and_cycles(locked):
    pins, installed, project = locked
    installed[2].requires += [
        "not-installed; python_version<'3'",
        "unselected; extra=='dev'",
        "transitive[chosen]",
    ]
    installed[3].requires = [
        "demo",
        "extra-dep; extra=='chosen'",
        "unselected; extra=='other'",
    ]
    pins["extra-dep"] = "1.0"
    installed.append(distribution("extra-dep"))
    constraints.validate_locked(pins, installed, project)
    installed.pop()
    del pins["extra-dep"]
    with pytest.raises(ValueError, match="missing dependency: extra-dep"):
        constraints.validate_locked(pins, installed, project)


def test_url_declaration_cannot_be_verified_with_version_only(locked):
    pins, installed, project = locked
    project["project"]["dependencies"] = ["demo @ https://example.org/demo.whl"]
    with pytest.raises(ValueError, match="URL requirement"):
        constraints.validate_locked(pins, installed, project)


def test_new_compatible_upstream_release_does_not_break_locked_ci(
    locked, tmp_path, monkeypatch, capsys
):
    pins, installed, project = locked
    path = tmp_path / "constraints.txt"
    path.write_text(constraints.render_constraints(pins), encoding="utf-8")
    original = path.read_bytes()
    monkeypatch.setattr(constraints, "distributions", lambda: installed)
    monkeypatch.setattr(constraints.tomllib, "loads", lambda text: deepcopy(project))

    def forbid_resolution(*args):
        pytest.fail("mandatory locked verification must never resolve upstream")

    monkeypatch.setattr(constraints, "resolve_constraints", forbid_resolution)
    monkeypatch.setattr(constraints, "_run", forbid_resolution)
    assert constraints.main(["--verify-locked", "--constraints-file", str(path)]) == 0
    newer = {**pins, "demo": "2.0"}  # Still allowed by demo>=1,<3.
    monkeypatch.setattr(constraints, "resolve_constraints", lambda root: newer)
    assert constraints.main(["--check", "--constraints-file", str(path)]) == 1
    assert "demo expected 1.0 resolved 2.0" in capsys.readouterr().out
    assert constraints.main(["--verify-locked", "--constraints-file", str(path)]) == 0
    assert path.read_bytes() == original


@pytest.mark.parametrize(
    "error",
    [
        OSError("network unavailable"),
        subprocess.CalledProcessError(
            1, ["pip"], output="resolver log", stderr="TLS failed"
        ),
        subprocess.TimeoutExpired(["pip"], 300, output="resolver stalled"),
    ],
)
def test_freshness_errors_remain_visible(tmp_path, monkeypatch, capsys, error):
    path = tmp_path / "constraints.txt"
    path.write_text("demo==1.0\n", encoding="utf-8")

    def fail(root):
        raise error

    monkeypatch.setattr(constraints, "resolve_constraints", fail)
    assert constraints.main(["--check", "--constraints-file", str(path)]) == 2
    output = capsys.readouterr().out
    assert "operation failed" in output
    assert "constraints match" not in output
    if isinstance(error, subprocess.CalledProcessError):
        assert "TLS failed" in output and "resolver log" in output


@pytest.mark.parametrize(
    ("status", "message"),
    [
        (0, "constraints match"),
        (1, "dependency drift detected"),
        (2, "operation failed: TLS error"),
        (97, "unexpected interpreter failure"),
    ],
)
def test_scheduled_report_preserves_output_and_failure(tmp_path, status, message):
    bash = shutil.which("bash")
    if not bash or os.name == "nt":
        pytest.skip("exercise the GitHub Actions bash step on POSIX")
    workflow = yaml.safe_load(
        (constraints.ROOT / ".github/workflows/python-freshness.yml").read_text("utf-8")
    )
    step = next(s for s in workflow["jobs"]["freshness"]["steps"] if "run" in s)
    fake_python = tmp_path / "python"
    fake_python.write_text(
        f"#!/bin/sh\nprintf '%s\\n' {shlex.quote(message)} >&2\nexit {status}\n",
        encoding="utf-8",
    )
    fake_python.chmod(0o755)
    summary = tmp_path / "summary.md"
    result = subprocess.run(
        [bash, "-e", "-c", step["run"]],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
        env={
            **os.environ,
            "PATH": f"{tmp_path}:{os.environ['PATH']}",
            "GITHUB_STEP_SUMMARY": str(summary),
            "GITHUB_SHA": "reviewed-sha",
        },
    )
    assert result.returncode == status
    assert message in result.stdout
    assert message in (tmp_path / "python-freshness.txt").read_text("utf-8")
    assert f"exit status: {status}" in summary.read_text("utf-8")
    assert "reviewed-sha" in summary.read_text("utf-8")


def test_freshness_workflow_is_separate_read_only_and_retains_failed_report():
    workflow = yaml.load(
        (constraints.ROOT / ".github/workflows/python-freshness.yml").read_text(
            "utf-8"
        ),
        Loader=yaml.BaseLoader,
    )
    assert set(workflow["on"]) == {"schedule", "workflow_dispatch"}
    assert workflow["permissions"] == {"contents": "read"}
    job = workflow["jobs"]["freshness"]
    assert job["timeout-minutes"] == "15"
    artifact = next(
        step for step in job["steps"] if "upload-artifact@" in step.get("uses", "")
    )
    assert artifact["if"] == "always()"
    assert artifact["with"]["if-no-files-found"] == "error"
