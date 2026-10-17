"""Durable chaos, runtime, licensing and lifecycle boundaries reviewed in Wave 15."""

import subprocess
from pathlib import Path

import pytest
import yaml

from scripts.catalog import load_tools

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "data/tools/chaos-performance-engineering.yaml"
REPORT = "docs/maintenance/2026-10-17-wave-15-chaos-resilience-evidence-review.md"
COHORT = (
    "chaos-mesh",
    "chaos-toolkit",
    "chaosblade",
    "toxiproxy",
    "pumba",
    "kube-monkey",
    "kubeinvaders",
    "chaos-monkey",
    "stress-ng",
    "iperf",
)
LICENCES = {
    "chaos-mesh": "Apache-2.0",
    "chaos-toolkit": "Apache-2.0",
    "chaosblade": "Apache-2.0",
    "toxiproxy": "MIT",
    "pumba": "Apache-2.0",
    "kube-monkey": "Apache-2.0",
    "kubeinvaders": "Apache-2.0",
    "chaos-monkey": "Apache-2.0",
    "stress-ng": "GPL-2.0-or-later",
    "iperf": "BSD-3-Clause-LBNL",
}


@pytest.fixture(scope="module")
def catalogue():
    return {t["id"]: t for t in load_tools()}


def test_report_has_exact_cohort_and_240_unique_field_decisions():
    report = (ROOT / REPORT).read_text(encoding="utf-8")
    assert {line[4:] for line in report.splitlines() if line.startswith("### ")} == set(
        COHORT
    )
    for tool_id in COHORT:
        section = (
            report.split(f"### {tool_id}\n", 1)[1]
            .split("\n### ", 1)[0]
            .split("\n## ", 1)[0]
        )
        rows = [line for line in section.splitlines() if line.startswith("| `")]
        fields = [line.split(" | ")[0] for line in rows]
        assert len(fields) == len(set(fields)) == 24
        assert all(
            "](https://" in row and ("CHANGED." in row or "UNCHANGED." in row)
            for row in rows
        )
        disposition = (
            "RETAIN REVIEW — INCONCLUSIVE"
            if tool_id == "chaos-monkey"
            else "CLEAR REVIEW"
        )
        assert f"**Disposition: {disposition}.**" in section


def test_wave15_changes_only_existing_cohort_and_preserves_provenance():
    base = subprocess.run(
        ["git", "merge-base", "HEAD", "origin/main"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if base.returncode:
        pytest.skip("Scope check requires origin/main")
    ref = base.stdout.strip()
    if (
        subprocess.run(
            ["git", "cat-file", "-e", f"{ref}:{REPORT}"],
            cwd=ROOT,
            capture_output=True,
            check=False,
        ).returncode
        == 0
    ):
        pytest.skip("Wave 15 is already in base")
    paths = subprocess.check_output(
        ["git", "diff", "--name-only", ref, "--", "data/tools"], cwd=ROOT, text=True
    ).splitlines()
    assert paths == [CANONICAL]
    before = {
        t["id"]: t
        for t in yaml.safe_load(
            subprocess.check_output(["git", "show", f"{ref}:{CANONICAL}"], cwd=ROOT)
        )
    }
    after = {
        t["id"]: t
        for t in yaml.safe_load((ROOT / CANONICAL).read_text(encoding="utf-8"))
    }
    assert before.keys() == after.keys()
    assert {i for i in before if before[i] != after[i]} == set(COHORT)
    for i in COHORT:
        assert set(before[i]["sources"]) <= set(after[i]["sources"])
        for field in (
            "id",
            "categories",
            "subcategories",
            "roles",
            "alternatives",
            "tags",
        ):
            assert before[i].get(field) == after[i].get(field)
    baseline = "config/link-audit-baseline.json"
    assert subprocess.check_output(
        ["git", "show", f"{ref}:{baseline}"], cwd=ROOT
    ).replace(b"\r\n", b"\n") == (ROOT / baseline).read_bytes().replace(b"\r\n", b"\n")


@pytest.mark.parametrize("tool_id", COHORT)
def test_actual_core_licence_docs_and_consistent_disposition(catalogue, tool_id):
    tool = catalogue[tool_id]
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == LICENCES[tool_id]
    licence = "COPYING" if tool_id == "stress-ng" else "LICENSE"
    assert any(
        url.endswith("/" + licence)
        and url.startswith(tool["repository_url"] + "/blob/")
        for url in tool["sources"]
    )
    assert tool["documentation_url"] in tool["sources"]
    assert tool["use_when"] and tool["avoid_when"] and tool["deployment_models"]
    retained = tool_id == "chaos-monkey"
    assert tool["needs_review"] is retained
    assert tool["status"] == ("needs-review" if retained else "active")
    assert tool["repository_archived"] is False


def test_netflix_support_is_unresolved_despite_active_declaration(catalogue):
    t = catalogue["chaos-monkey"]
    text = " ".join([t["summary"], *t["avoid_when"]])
    assert t["maturity"] == "unknown"
    assert all(
        term in text
        for term in ("Spinnaker", "MySQL", "cron", "inconclusive", "January 2025")
    )
    assert any(url.endswith("/OSSMETADATA") for url in t["sources"])
    assert any(url.endswith("/NOTICE") for url in t["sources"])


def test_iperf_is_esnet_v3_with_lbnl_clause_and_preserved_download_history(catalogue):
    t = catalogue["iperf"]
    assert t["name"] == "iPerf3 (ESnet)"
    assert (
        t["official_url"] == t["documentation_url"] == "https://software.es.net/iperf/"
    )
    assert t["repository_url"] == "https://github.com/esnet/iperf"
    assert "https://iperf.fr/iperf-download.php" in t["sources"]
    assert "enhancement clause" in t["summary"] and "bundled-component" in t["summary"]
    assert "https://spdx.org/licenses/BSD-3-Clause-LBNL.html" in t["sources"]
    assert all(
        term in " ".join(t["avoid_when"])
        for term in ("iPerf2", "incompatible", "Windows", "bandwidth")
    )


def test_stress_ng_or_later_grant_and_benchmark_limit(catalogue):
    t = catalogue["stress-ng"]
    assert any(url.endswith("/stress-ng.c") for url in t["sources"])
    assert "precise benchmark" in t["summary"]
    assert all(
        term in " ".join(t["avoid_when"])
        for term in ("thermal", "root", "OOM", "host impact")
    )


@pytest.mark.parametrize(
    ("tool_id", "terms"),
    [
        (
            "chaos-mesh",
            ("privileged", "rbac", "selectors", "authentication", "production"),
        ),
        (
            "chaos-toolkit",
            ("third-party extension", "licence", "rollback", "credentials"),
        ),
        ("chaosblade", ("executor", "runtime", "process-attach", "http", "recovery")),
        ("toxiproxy", ("udp", "tcp", "unauthenticated", "bearer token")),
        (
            "pumba",
            ("docker socket", "net_admin", "containerd", "rootful podman", "crd"),
        ),
        (
            "kube-monkey",
            (
                "pod-deletion",
                "rbac",
                "recovery",
                "cloud-instance",
                "poddisruptionbudget",
            ),
        ),
        (
            "kubeinvaders",
            ("clusterrolebinding", "tls", "credentials", "kubevirt", "node chaos"),
        ),
    ],
)
def test_privilege_and_execution_boundaries(catalogue, tool_id, terms):
    text = " ".join(catalogue[tool_id]["avoid_when"]).lower()
    assert all(term in text for term in terms)


def test_mesh_and_blade_keep_separate_control_planes(catalogue):
    assert "CRDs" in catalogue["chaos-mesh"]["summary"]
    assert "daemon" in catalogue["chaos-mesh"]["summary"]
    assert "separate" in catalogue["chaosblade"]["summary"]
    assert "operator" in catalogue["chaosblade"]["summary"]


def test_pumba_current_runtime_scope_and_kubeinvaders_node_jobs(catalogue):
    assert all(
        term in catalogue["pumba"]["summary"]
        for term in ("Docker", "containerd", "Podman", "Linux")
    )
    assert "node chaos jobs" in catalogue["kubeinvaders"]["summary"]
    assert "simulated demo" in catalogue["kubeinvaders"]["summary"]
