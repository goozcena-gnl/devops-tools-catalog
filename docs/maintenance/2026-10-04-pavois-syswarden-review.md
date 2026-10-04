# Pavois and SysWarden maintainer review

Primary sources were checked on 2026-10-04. Pavois's
[handbook](https://pavois.dev/en/handbook/),
[README](https://github.com/stephrobert/pavois/blob/main/README.md),
[Apache-2.0 licence](https://github.com/stephrobert/pavois/blob/main/LICENSE),
and current repository history support the Linux runtime compliance,
standards mapping, reviewable hardening, and emerging maturity recorded here.
No equivalent canonical identity or alias was found.

SysWarden's [README](https://github.com/duggytuxy/syswarden/blob/main/README.md)
supports host-local nftables enforcement, host telemetry, out-of-band WAAP,
authenticated HA, and the stated adoption boundaries. Its current release
history supports active maintenance. The existing canonical ID and legacy
provenance are preserved.

SysWarden's [licence](https://github.com/duggytuxy/syswarden/blob/main/LICENSE)
contains the GPLv3 text, but the inspected primary sources do not establish an
applied `only` versus `or-later` grant. The unsupported `GPL-3.0-only` SPDX
claim was removed and `needs_review: true` retained pending an explicit upstream
notice. The OSS licence model remains supported; no variant is guessed.

Catalogue quality run
[35707774156](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/35707774156)
failed in `validate` / `Run tests`: nine failures assumed the current catalogue
would always have 1,423 records, and one found eleven stale generated files.
Historical identity tests now protect the exact immutable v0.5 baseline,
including its Wave 4 fingerprint, while allowing additions. Negative coverage
rejects baseline deletion/replacement and duplicate IDs. Generated pages are
produced by `python -m scripts.generate_docs`.

No retained link-audit reports or historical link blockers were changed. A
representative full network audit was not performed in this session.
