# ElectrosynthesisPapers

A fully automated, continuously updated public index of **organic
electrosynthesis research** — synthesis in which electricity itself is the
reagent. Anodic oxidation and cathodic reduction, electrochemical C–H
functionalization and cross-coupling, paired and mediated electrolysis,
electrophotochemistry, asymmetric electrosynthesis, decarboxylative and radical
electrochemistry, flow electrosynthesis and scale-up, and the cell and
electrode design behind them.

The scope is **electrochemistry used as a reaction condition to make
molecules** — the Baran / Waldvogel / Moeller / Yoshida line of work.
Electrochemistry that is not synthesis is filtered out: batteries and
supercapacitors, fuel cells, water-splitting and HER/OER/ORR electrocatalysis,
corrosion, electroplating, and electroanalytical sensing.

Sister project of
[FlowChemistryPapers](https://github.com/GuruprakashMP/flow-chemistry-papers),
[PhotocatalysisPapers](https://github.com/GuruprakashMP/photocatalysis-papers),
[MechanochemistryPapers](https://github.com/GuruprakashMP/mechanochemistry-papers)
and
[DataDrivenChemistryPapers](https://github.com/GuruprakashMP/ddc-papers) —
same architecture, different scientific scope.

* **No papers are hosted.** Only bibliographic metadata (title, authors,
  journal, date, DOI, link); every card links to the original publisher.
* **Zero dependencies.** Standard-library Python; JSON + static HTML,
  perfect for GitHub Pages.
* **Fully automatic.** A GitHub Actions workflow collects, deduplicates,
  classifies, rebuilds the site and commits — every day.

## Quick start (local)

```bash
cd electrochemistry_papers
# Windows:  set PYTHONPATH=src        PowerShell:  $env:PYTHONPATH="src"
export PYTHONPATH=src

python -m ddc run            # collect + rebuild the website
python -m ddc run --days 7   # look further back
python -m ddc backfill --from 1960   # historical harvest (year batches!)
python -m ddc build          # rebuild website only
python -m ddc stats          # index statistics
python -m unittest discover -s tests
```

(On this machine Python 3.9 is the `py` launcher; `python` is not on PATH —
use `py -m ddc ...`.)

The backfill starts at **1960**, covering the modern era of preparative
organic electrochemistry from Baizer's adiponitrile process onward. Run it in
year-sized ranges via the "Electrosynthesis historical backfill" GitHub
Actions workflow: OpenAlex allows roughly 15k record fetches per runner per
day, and every workflow run gets a fresh runner. Each run checkpoints, so
interrupting and re-running is safe.

## How papers are selected

A paper is indexed only when **electrochemistry is being used to make organic
molecules**, evidenced by unambiguous vocabulary (electrosynthesis,
electroorganic, anodic oxidation, cathodic reduction, paired/mediated/indirect
electrolysis, electrochemical C–H functionalization, Kolbe electrolysis, Shono
oxidation, electrophotocatalysis, ...). Supporting terms (undivided cell,
sacrificial anode, supporting electrolyte, RVC/BDD electrodes, TEMPO and other
mediators, cyclic voltammetry, substrate scope, gram-scale, late-stage
functionalization) refine the 0–100 relevance score and assign multiple
categories. Neighbouring electrochemical fields that are not synthesis are
penalised out. Tune the vocabulary in `src/ddc/keywords.py`.

## Sources

Direct: **arXiv**, **ChemRxiv**. Aggregators: **Crossref**, **OpenAlex**,
**PubMed**, **Europe PMC**, **Semantic Scholar**, **DOAJ** — which legally
carry the metadata of every DOI-issuing publisher (ACS, RSC, Wiley, Springer
Nature, Elsevier, MDPI, ...).

## Deploying

1. Push this folder's contents to a public GitHub repository
   (e.g. `electrosynthesis-papers`).
2. **Settings → Pages → Deploy from a branch → `main` / root → Save.**
3. Live at `https://<user>.github.io/<repo>/` a minute later; the daily
   workflow keeps it growing with no maintenance.

See [ARCHITECTURE.md](ARCHITECTURE.md) for design decisions,
[PROJECT_STATUS.md](PROJECT_STATUS.md) for current state, and
[CHANGELOG.md](CHANGELOG.md) for history.
