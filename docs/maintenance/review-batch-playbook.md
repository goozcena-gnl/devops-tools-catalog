# Evidence-review batch playbook

This playbook converts catalogue review debt into small, evidence-backed
contribution opportunities without creating an issue for every record.

## When to open a batch

Open a batch only when the canonical data and generated review-debt inventory
show a coherent group that can be reviewed with the same evidence question.
Examples include canonical identity, lifecycle, licensing, archived upstreams,
or a single taxonomy area. Do not open speculative batches merely to increase
issue activity.

Keep the public queue to a few active batches. Close, refill, or rescope that
queue based on maintainer review capacity.

## Batch sizes

- Beginner-friendly metadata or link review: 5–15 records.
- Experienced lifecycle, ownership, or licence review: 10–30 records only when
  the evidence boundary is genuinely consistent.
- Smaller batches are appropriate when legal or product/repository boundaries
  require individual judgement.

A batch is not `good first issue` work when resolving it requires interpreting
licence boundaries, product ownership, forks, acquisitions, or conflicting
lifecycle signals.

## Required issue contract

Every evidence-review issue must state:

- the exact question and fields in scope;
- every canonical record ID;
- expected primary evidence and acceptable official sources;
- canonical files likely to change;
- validation and documentation-generation commands;
- completion criteria, including how to record an inconclusive result;
- an explicit instruction not to infer or guess metadata.

The issue should link the current deterministic inventory from
`python -m scripts.review_debt` when its scope derives from review debt. Link
the canonical URL-maintenance tracker when the batch is extracted from that
tracker so work is not duplicated.

## Completion states

**Resolved** means the canonical record contains the checked primary evidence,
the scoped metadata is supported, generated documentation is current, and all
validation passes.

**Inconclusive** means primary sources were checked but do not support a safe
factual update. Record the sources and outcome in the pull request, preserve
the current unresolved value, and retain `needs_review: true`.

An HTTP success, redirect, repository visibility, or plausible search result is
never sufficient by itself to assert ownership, active lifecycle, or licence.
