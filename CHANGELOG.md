# Changelog

All notable changes to ElectrosynthesisPapers.

## [1.1.0] — 2026-07-30

Historical backfill 1960→2026 complete and verified: **14,947 papers**
indexed, covering organic electrosynthesis from the Baizer adiponitrile era
to today.

### Added
- Full topic sweep of all 67 years, driven newest-first by a local monitor.
  **Zero `INCOMPLETE` years.**
- Pioneer sweep (25 author entries, +1,254 papers) run first as its own
  workflow run.

### Notes
- OpenAlex throttling is transient, not a hard daily cap: 1974 aborted with
  `12 consecutive failed queries` about two hours past the reliable
  05:00-11:00 UTC window, produced no year marker at all, and succeeded on
  the retry 45 minutes later. A missing marker is therefore treated as a bad
  batch, never as success.
- Author names were canonical from ingestion — `tools/normalize_authors.py`
  finds nothing to migrate, confirming the inherited fix works on a
  from-scratch index.

## [1.0.0] — 2026-07-30

Initial release, adapted from the
[FlowChemistryPapers](https://github.com/GuruprakashMP/flow-chemistry-papers)
codebase — the newest hardened version of the family architecture
(stdlib-only pipeline, 8 metadata collectors, resumable OpenAlex backfill with
a fetch-side checkpoint, INCOMPLETE-year flagging, peer-review-artifact and
corrupt-OSTI-merge collector guards, author-name canonicalization, static site
with progressive loading).

### Changed from the parent project

- Scope: **organic electrosynthesis** — electrochemistry used as the reaction
  condition to make molecules (Baran / Waldvogel / Moeller / Yoshida line of
  work) instead of flow chemistry. Deliberately NOT a general electrochemistry
  index: batteries, supercapacitors, fuel cells, water-splitting and
  HER/OER/ORR electrocatalysis, corrosion, electroplating and electroanalytical
  sensing are all filtered out.
- Classifier: PRIMARY electrosynthesis vocabulary required (electrosynthesis,
  electroorganic, anodic oxidation, cathodic reduction, electrooxidative/
  electroreductive, paired/mediated/indirect electrolysis, electrochemical C–H
  and cross-coupling, Kolbe electrolysis, Shono oxidation, cation pool,
  electrophotocatalysis, undivided cell, sacrificial anode, ...); SUPPORT
  vocabulary (electrode materials, supporting electrolyte, TEMPO and other
  mediators, voltammetry, substrate scope, gram-scale, late-stage
  functionalization, total synthesis) refines score/categories; NEGATIVE
  vocabulary rejects the non-synthetic electrochemical fields above.
- 18 electrosynthesis-specific categories.
- All collector and backfill queries rewritten for organic electrosynthesis.
- Pioneers list: Phil Baran, Siegfried Waldvogel, Hans Schäfer, Kevin Moeller,
  R. Daniel Little, Toshio Fuchigami, Hai-Chao Xu, Song Lin, Lutz Ackermann,
  Aiwen Lei, Manuel Baizer, Robert Francke, Kevin Lam, Tian-Sheng Mei,
  Cheng-Chu Zeng, Shelley Minteer, Christian Amatore, Jun-ichi Yoshida,
  Dennis Peters, Sebastian Beil, Timothy Noël, Gabriele Laudadio and more —
  with accented and initial spelling variants listed side by side, because
  the OpenAlex quoted-phrase author search is spelling-exact.
- Backfill default start year: 1960 (the Baizer adiponitrile era onward).
- Site branding: ElectrosynthesisPapers.

### Inherited hardening (kept from the parent, domain-independent)

- **Fetch-side checkpoint** (`data/state/backfill_progress.json`): completed
  (year, query) pairs are skipped on re-runs.
- Backfill years with any transiently failed query log `INCOMPLETE` instead
  of `done`, so a driver re-runs them.
- Collector guards drop transparent-peer-review artifacts and corrupted OSTI
  merges at ingestion.
- Author names are canonicalized at ingestion (`models.normalize_author`), so
  one researcher maps to one author page; `tools/normalize_authors.py` can
  re-canonicalize stored shards and is self-converging.
