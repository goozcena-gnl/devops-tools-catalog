from pathlib import Path

from scripts.catalog import ROOT
from scripts.python_constraints import diff_constraints, parse_pinned_requirements


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
