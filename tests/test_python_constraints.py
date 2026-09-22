from pathlib import Path

import pytest

import scripts.python_constraints as python_constraints
from scripts.catalog import ROOT
from scripts.python_constraints import (
    check_constraints,
    diff_constraints,
    parse_pinned_requirements,
    render_constraints,
    resolve_constraints_path,
    write_constraints,
)


def test_parse_pinned_requirements_normalizes_names_and_ignores_tooling() -> None:
    parsed = parse_pinned_requirements(
        [
            "# comment",
            "PyYAML==6.0.2",
            "jsonschema==4.25.1",
            "devops-tools-catalog==0.5.0",
            "setuptools==80.9.0",
        ]
    )

    assert parsed == {
        "jsonschema": "4.25.1",
        "pyyaml": "6.0.2",
    }


def test_diff_constraints_reports_missing_added_and_changed_versions() -> None:
    missing, added, changed = diff_constraints(
        {"a-package": "1.0.0", "b-package": "2.0.0"},
        {"b-package": "2.1.0", "c-package": "3.0.0"},
    )

    assert missing == ["a-package"]
    assert added == ["c-package"]
    assert changed == ["b-package"]


def test_quality_workflow_checks_and_uses_constraints() -> None:
    workflow = (ROOT / ".github" / "workflows" / "quality.yml").read_text(
        encoding="utf-8"
    )

    assert "python -m scripts.python_constraints --check" in workflow
    assert "-c config/python-constraints-3.12.txt hatchling editables" in workflow
    assert (
        "--no-build-isolation -c config/python-constraints-3.12.txt -e '.[dev]'"
        in workflow
    )


def test_link_check_workflow_uses_constraints() -> None:
    workflow = (ROOT / ".github" / "workflows" / "link-check.yml").read_text(
        encoding="utf-8"
    )

    assert "python -m scripts.python_constraints --check" in workflow
    assert "-c config/python-constraints-3.12.txt hatchling editables" in workflow
    assert "--no-build-isolation -c config/python-constraints-3.12.txt -e ." in workflow


def test_constraints_file_contains_only_pinned_requirements() -> None:
    constraints_path = ROOT / "config" / "python-constraints-3.12.txt"
    parsed = parse_pinned_requirements(
        constraints_path.read_text(encoding="utf-8").splitlines()
    )

    assert constraints_path == Path(ROOT / "config" / "python-constraints-3.12.txt")
    assert parsed


def test_resolve_constraints_path_uses_root_for_relative_paths() -> None:
    path = resolve_constraints_path(Path("config/custom-constraints.txt"), ROOT)

    assert path == ROOT / "config" / "custom-constraints.txt"


def test_write_constraints_resolves_relative_path_against_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    target = root / "config" / "custom-constraints.txt"
    target.parent.mkdir()

    def fake_resolve_constraints(resolved_root: Path) -> dict[str, str]:
        assert resolved_root == root
        return {"pytest": "9.1.1"}

    monkeypatch.setattr(
        python_constraints,
        "resolve_constraints",
        fake_resolve_constraints,
    )

    exit_code = write_constraints(Path("config/custom-constraints.txt"), root)

    assert exit_code == 0
    assert target.read_text(encoding="utf-8") == render_constraints({"pytest": "9.1.1"})


def test_check_constraints_resolves_relative_path_against_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "repo"
    constraints_dir = root / "config"
    constraints_dir.mkdir(parents=True)
    target = constraints_dir / "custom-constraints.txt"
    target.write_text("pytest==9.1.1\n", encoding="utf-8")

    def fake_resolve_constraints(resolved_root: Path) -> dict[str, str]:
        assert resolved_root == root
        return {"pytest": "9.1.1"}

    monkeypatch.setattr(
        python_constraints,
        "resolve_constraints",
        fake_resolve_constraints,
    )

    exit_code = check_constraints(Path("config/custom-constraints.txt"), root)

    assert exit_code == 0


def test_main_check_custom_constraints_path_is_side_effect_free(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    constraints_path = tmp_path / "nested" / "constraints.txt"
    captured: dict[str, Path] = {}

    def fake_check_constraints(path: Path, root: Path = ROOT) -> int:
        captured["path"] = path
        return 0

    monkeypatch.setattr(
        python_constraints,
        "check_constraints",
        fake_check_constraints,
    )

    exit_code = python_constraints.main(
        ["--check", "--constraints-file", str(constraints_path)]
    )

    assert exit_code == 0
    assert captured["path"] == constraints_path
    assert not constraints_path.parent.exists()
