# Deferred catalogue corrections — 2026-09-03

This maintenance wave corrects four pre-existing catalogue records:
`mcp-server-kubernetes`, `floci`, `opnsense`, and `xcp-ng`. It adds no canonical
IDs and removes none.

The corrections use official product sites, documentation, canonical repositories,
and official licence material. OPNsense and XCP-ng remain `oss`, but do not receive
a single `license_spdx` value because each product distribution contains components
under multiple licences. Their paid support or business offerings are represented
with `commercial_offering: true`, not by changing the community product to
`open-core`.

## N1a supersession boundary

The historical N1a baseline, result commits, manifest, evidence ledger, selector,
work-item accounting, and historical diff remain unchanged. N1a reviewed only the
`official_url` of `mcp-server-kubernetes`; that accepted URL remains unchanged.

The current-state persistence guard now permits a later correction for exactly these
fields of `mcp-server-kubernetes`:

- `repository_url`
- `license_spdx`
- `status`
- `needs_review`

All other N1a protections, including `official_url` and `license_model`, continue to
be enforced. The focused regression test asserts both the exact allowlist and the
continued rejection of an unrelated protected-field change.
