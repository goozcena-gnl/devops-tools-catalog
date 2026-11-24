# Python dependency freshness review — 2026-11-24

## Disposition and bounded scope

**Candidate A: local technical PASS (Windows and Linux); full freshness remains unresolved.** This ledger records the evidence available before publication. It does not authorize a commit, push, pull request, merge, release, workflow dispatch or change to the freshness gate. The future PR is independent of the completed #204 / #205 work; #206 remains open.

- Base main: `6d26bb1cad133755b6433447ece4b9435af85195`; tree `ad3b73510fd35cde182dc7e01a45c44930e325d1`.
- Original constraints blob: `f0b4b0397f47b73644b775adf7fcee0d75710ccc`.
- Candidate constraints blob: `2115ff152af440bd293e0fc826d0f174f5c59c91`.
- Candidate constraints SHA256: `251ae941076f7d8dedf3c46f65990eb6fbcca0dff25a84c60d9500cad8a1a1ab`.
- Exact lock-only patch SHA256: `ce99c98674668871847f834e47a287fd5892d7e83a579940f0ddf755f0f5a4d8`.
- Two allowed paths: `config/python-constraints-3.12.txt` and this new ledger. Exactly three pin replacements; 16 unchanged; no added or removed Linux pins (19 total). No canonical record IDs changed. All 327 other original tracked files protected, including the baseline blob `a834e2af711693def40078a55e31dfeb29bee2c7`, data tree `0a9784e3afe9cf71a04b2ffb1a51e4e48478e47a`, workflows, schema, scripts, tests and generated docs. Windows-only `colorama==0.4.6` remains an external overlay (20 local pins).

## Trigger and upstream evidence

[Scheduled freshness run 45431955925](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45431955925), job `138579435278`, failed on exact base with exit 1 (dependency drift, not a resolver error). [Report artifact 14940055325](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45431955925/artifacts/14940055325); reported archive SHA256 `b648b503c2eaa8a9edd1f6dd9aaf828e08e26b00a303854cb71a7fe25ad1d6f9`. The six integration checks on base, including [strict link audit #112](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45429743859), passed. The freshness failure is separate; main is not globally green.

| Package | Base | Observed upstream | Candidate A | Disposition |
|---|---|---|---|---|
| packaging | 26.3 | 26.4 | 26.4 | Local validation PASS; requirement/specifier/marker verification |
| PyYAML | 6.0.3 | 6.0.4 | 6.0.3 | HOLD; semantic regression |
| Ruff | 0.17.5 | 0.17.6 | 0.17.6 | Local lint and format PASS |
| TOMLKit | 0.15.2 | 0.15.3 | 0.15.3 | Local backend/build validation PASS |

Official release evidence: [packaging 26.4](https://github.com/pypa/packaging/releases/tag/26.4), [PyYAML 6.0.4](https://github.com/yaml/pyyaml/releases/tag/6.0.4), [Ruff 0.17.6](https://github.com/astral-sh/ruff/releases/tag/0.17.6), [TOMLKit 0.15.3](https://github.com/python-poetry/tomlkit/releases/tag/0.15.3). Packaging changes parsing and marker validation; Ruff changes active lint families; TOMLKit changes preservation and serialization of TOML data. PyYAML fixes exponential merge-key expansion and updates bundled LibYAML, but the semantic regression below blocks this upgrade.

## PyYAML #953 — reproducible HOLD

[Upstream issue #953](https://github.com/yaml/pyyaml/issues/953) describes merge-key precedence. [Release source 6.0.4](https://github.com/yaml/pyyaml/blob/6.0.4/lib/yaml/constructor.py) uses identity-based deduplication in `flatten_mapping`. The Windows and Linux wheel experiments independently reproduced six failures out of 14 probes **on each platform**, with LibYAML available. Both baseline and Candidate A (6.0.3) passed all 14 probes on each platform.

| Loader | Case | Expected | Windows 6.0.4 | Linux 6.0.4 |
|---|---|---|---|---|
| SafeLoader | first-wins `kk` | 1 | 3 | 3 |
| SafeLoader | first-wins `status` | 1 | 3 | 3 |
| SafeLoader | nested merge | status active, count 3 | status historical, count 3 | status historical, count 3 |
| CSafeLoader | first-wins `kk` | 1 | 3 | 3 |
| CSafeLoader | first-wins `status` | 1 | 3 | 3 |
| CSafeLoader | nested merge | status active, count 3 | status historical, count 3 | status historical, count 3 |

The other eight probes passed (including single-character first-wins and explicit overrides). This is silent data corruption potential, not a demonstrated change to current catalogue records. The 31 YAML semantic digests (30 tool files plus taxonomy) were identical across the 12 environments. Switching to CSafeLoader is not a workaround. The experimental PyYAML environment's ordinary targeted pytest suite passed 207 tests on both platforms, so that suite alone does not establish merge precedence correctness. Retaining 6.0.3 also retains the known risk of expensive YAML merge expansion; only trusted/bounded YAML should be processed pending a reviewed fix. No CVE absence claim is made. Revisit with a fixed upstream release, the same probes, security assessment and full validation; do not introduce an undocumented exception or silently regenerate pins.

## Cross-platform evidence

| Environment | Windows Python 3.12.10 | Linux WSL2 Python 3.12.3 |
|---|---|---|
| Baseline | 1026 passed, 8 skipped | 1030 passed, 4 skipped |
| Packaging only | 46 passed, 4 skipped | 50 passed |
| PyYAML only | 207 passed; 6/14 YAML probes failed | 207 passed; 6/14 YAML probes failed |
| Ruff only | lint and format PASS | lint and format PASS |
| TOMLKit only | 46 passed, 4 skipped | 50 passed |
| Candidate A | 1026 passed, 8 skipped | 1030 passed, 4 skipped |

Windows has four additional POSIX-only skips. Candidate A and baseline ran `pip check`, `scripts.python_constraints --verify-locked` (platform-local constraints), Ruff lint/format, full pytest, generation check, generation and recheck, catalogue validation, review-debt inventory and build. All passed. Six project wheels (baseline, TOMLKit, Candidate A on both platforms) had identical internal content and metadata. Candidate A has 1425 unique records, 30 categories, 533 review flags, 65 unknown license models, 768 unknown maturities; review debt unchanged. No canonical YAML change. The earlier full tests concern the lock-only candidate, not this new ledger. The final two-path worktree must be checked before publication; no CI result for a future commit is claimed here.

## Supply chain and limitations

Operator-verified wheel hashes and PyPI metadata, including platform-specific wheels, were recorded before offline installations. The two exported reports show 24 Windows / 23 Linux package-version queries to OSV, all successful, with no OSV or PyPI advisories returned and no unknown query statuses. Provenance available (not cryptographically verified): 15 on each platform; unavailable: 9 Windows / 8 Linux. These are point-in-time observations, not a proof of absence of vulnerabilities. The evidence export omits third-party wheel bytes and raw PyPI/provenance responses; their recorded hashes were reconciled, not independently recomputed from the wheels by the reviewer. Six built project wheels were included. Publisher signatures were not verified. No complete repository security alert inventory was examined.

Exported evidence archive SHA256 (operator exports, independently recalculated; archives stay outside repository):

- Windows `e46e3214817c185e24afa41450b41be877893c4f08a5ffeba5f27e91e8ce4e00`.
- Linux `e7ba752a2fc5a71cad38fd28769a07e2cbb5535ce0872358ef62bc36ab9dd3cd`.

Each archive has 115 files, 114 checked against the included manifest (the manifest itself is covered by the archive digest). Original manifests have 185 Windows / 182 Linux entries; 71 / 68 entries were not exported. The operator verified the full manifests before export. Both exports independently contain identical candidate lock bytes and lock-only patch bytes.

## Residual freshness and follow-up gates

The offline candidate freshness check returned exit 1 for exactly `pyyaml expected 6.0.3 resolved 6.0.4`. Live resolution may drift again; it must not be reported as passed based on this offline snapshot. No workflow exception, `continue-on-error`, constraint widening, automatic regeneration, pin removal or baseline edit is proposed. A future Draft PR must disclose the expected residual failure and evaluate any new drift separately. Required checks and branch protection must be examined before any merge decision; no bypass requested. Reassess security and PyYAML upstream at that time. Run the final exact-SHA CI and separate strict link audit before a human merge decision; no new network link audit has been run for this candidate yet. The previous #112 is base evidence only.
