# Project Status

_Last updated: 2026-07-30 (initial release)_

## Completed

- [x] Codebase adapted from the FlowChemistryPapers template — the newest
      hardened version of the family architecture, keeping the
      peer-review-artifact and corrupt-OSTI-merge collector guards,
      INCOMPLETE-year flagging, the fetch-side backfill checkpoint, and
      author-name canonicalization (`models.normalize_author` +
      `tools/normalize_authors.py`).
- [x] Organic-electrosynthesis classifier: PRIMARY terms (electrosynthesis,
      electroorganic, anodic oxidation, cathodic reduction,
      electrooxidative/electroreductive, paired/mediated/indirect
      electrolysis, electrochemical C–H and cross-coupling, Kolbe, Shono,
      cation pool, electrophotocatalysis, undivided cell, sacrificial
      anode...) required; SUPPORT terms (electrodes, supporting electrolyte,
      mediators, voltammetry, substrate scope, gram-scale, late-stage
      functionalization) refine score and categories; NEGATIVE terms reject
      the electrochemistry that is not synthesis — batteries and
      supercapacitors, fuel cells, water splitting and HER/OER/ORR
      electrocatalysis, corrosion, electroplating, electroanalytical sensing.
- [x] 17 electrosynthesis categories.
- [x] Collector + backfill queries rewritten for organic electrosynthesis.
- [x] Pioneers list: Baran, Waldvogel, Schäfer, Moeller, Little, Fuchigami,
      Xu, Lin, Ackermann, Lei, Baizer, Francke, Lam, Mei, Zeng, Minteer,
      Amatore, Yoshida, Peters, Beil, Noël, Laudadio and more
      (config/pioneers.json), with accented/initial spelling variants listed
      side by side because the OpenAlex author search is spelling-exact.

## Known issues (inherited environment quirks)

- Local machine: arXiv fails (missing SSL certs) and ChemRxiv 403s
  (Cloudflare) — both work/degrade gracefully in GitHub Actions.
- Semantic Scholar keyless tier rate-limits; collector skips gracefully.
- OpenAlex throttling: throttles in long daily windows (~11:00–05:00 UTC)
  regardless of runner IP; only ~05:00–11:00 UTC is reliable. Each run also
  has a fetch budget (~15k records) — the fetch-side checkpoint
  (data/state/backfill_progress.json) makes retries spend it only on missing
  queries. The pioneer sweep alone costs ~12k fetches — never bundle it with
  a topic-year range in one run.
- Throttling appears **shared across the sibling paper-index projects**:
  never run two backfill chains at once. Check `gh run list` on
  ddc-papers, photocatalysis-papers, mechanochemistry-papers and
  flow-chemistry-papers before starting one.
- OneDrive can silently revert a file write in this tree *after* it has read
  back correctly; `tools/normalize_authors.py` is self-converging because of
  it. Keep that in mind for any bulk rewrite here.
