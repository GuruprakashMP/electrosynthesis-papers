"""Keyword knowledge base for classification.

Three vocabularies drive the relevance decision:

* ``PRIMARY_TERMS`` — organic-electrosynthesis vocabulary. A paper must show
  strong evidence here to be indexed at all: this is the project's core rule,
  *electrochemistry used as the reaction condition to make organic molecules*
  (Baran-, Waldvogel-, Moeller-style e-synthesis).
* ``SUPPORT_TERMS`` — cell hardware, mediators, electroanalytical methods and
  the synthetic-organic vocabulary that refine the score and assign categories.
* ``NEGATIVE_TERMS`` — signals the paper belongs to a neighbouring
  electrochemical field that is NOT synthesis: batteries and supercapacitors,
  fuel cells, water splitting / HER-OER-ORR electrocatalysis, corrosion,
  electroplating, electroanalytical sensing.  ``penalty`` points.

Weights: 4 = unambiguous ("electrosynthesis", "anodic oxidation", "paired
electrolysis"), 3 = strong, 2 = supportive, 1 = weak/generic.  Tags become the
visible chips on paper cards; categories group papers for browsing.
"""

from __future__ import annotations

from typing import Dict, Tuple

# ---------------------------------------------------------------------------
# Primary organic-electrosynthesis terms — required evidence
# ---------------------------------------------------------------------------
PRIMARY_TERMS: Dict[str, Tuple[int, str, str]] = {
    # phrase: (weight, tag, category)
    # --- the field's own names -------------------------------------------
    "electrosynthesis": (4, "Electrosynthesis", "General Electrosynthesis"),
    "electrosynthetic": (4, "Electrosynthesis", "General Electrosynthesis"),
    "electro-synthesis": (4, "Electrosynthesis", "General Electrosynthesis"),
    "organic electrosynthesis": (4, "Organic Electrosynthesis", "General Electrosynthesis"),
    "electroorganic": (4, "Electroorganic", "General Electrosynthesis"),
    "electro-organic": (4, "Electroorganic", "General Electrosynthesis"),
    "organic electrochemistry": (4, "Organic Electrochemistry", "General Electrosynthesis"),
    "synthetic organic electrochem": (4, "Organic Electrochemistry", "General Electrosynthesis"),
    "electrolytic synthesis": (4, "Electrolytic Synthesis", "General Electrosynthesis"),
    "preparative electrolysis": (4, "Preparative Electrolysis", "General Electrosynthesis"),
    "preparative-scale electrolysis": (4, "Preparative Electrolysis", "General Electrosynthesis"),
    "electrochemical synthesis of": (3, "Electrochemical Synthesis", "General Electrosynthesis"),
    "electrochemically driven": (3, "Electrochemically Driven", "General Electrosynthesis"),
    "electrochemically enabled": (4, "Electrochemically Enabled", "General Electrosynthesis"),
    "electrochemically generated": (3, "Electrogenerated Species", "Mechanism & Electroanalysis"),
    # --- anodic / cathodic processes -------------------------------------
    "anodic oxidation": (4, "Anodic Oxidation", "Anodic Oxidation"),
    "anodic coupling": (4, "Anodic Coupling", "Anodic Oxidation"),
    "anodic substitution": (4, "Anodic Substitution", "Anodic Oxidation"),
    "anodic cyclization": (4, "Anodic Cyclization", "Anodic Oxidation"),
    "electrooxidative": (4, "Electrooxidative", "Anodic Oxidation"),
    "electro-oxidative": (4, "Electrooxidative", "Anodic Oxidation"),
    "electrochemical oxidative": (4, "Electrooxidative", "Anodic Oxidation"),
    "cathodic reduction": (4, "Cathodic Reduction", "Cathodic Reduction"),
    "cathodic coupling": (4, "Cathodic Coupling", "Cathodic Reduction"),
    "electroreductive": (4, "Electroreductive", "Cathodic Reduction"),
    "electro-reductive": (4, "Electroreductive", "Cathodic Reduction"),
    "electrochemical reductive": (4, "Electroreductive", "Cathodic Reduction"),
    "reductive electrolysis": (4, "Reductive Electrolysis", "Cathodic Reduction"),
    "oxidative electrolysis": (4, "Oxidative Electrolysis", "Anodic Oxidation"),
    # --- named reactions / classic e-synthesis ---------------------------
    "kolbe electrolysis": (4, "Kolbe Electrolysis", "Decarboxylative & Radical Reactions"),
    "kolbe coupling": (4, "Kolbe Electrolysis", "Decarboxylative & Radical Reactions"),
    "non-kolbe": (4, "Non-Kolbe", "Decarboxylative & Radical Reactions"),
    "shono oxidation": (4, "Shono Oxidation", "Anodic Oxidation"),
    "cation pool": (4, "Cation Pool", "Mechanism & Electroanalysis"),
    "cation flow": (4, "Cation Flow", "Flow Electrosynthesis & Scale-up"),
    "electrogenerated base": (4, "Electrogenerated Base", "Mediated & Indirect Electrolysis"),
    "electrogenerated acid": (4, "Electrogenerated Acid", "Mediated & Indirect Electrolysis"),
    # --- coupling / functionalization under electrochemical conditions ---
    "paired electrolysis": (4, "Paired Electrolysis", "Paired Electrolysis"),
    "paired electrochemical": (4, "Paired Electrolysis", "Paired Electrolysis"),
    "electrochemical c-h": (4, "Electrochemical C-H", "C-H Functionalization"),
    "electrochemical c–h": (4, "Electrochemical C-H", "C-H Functionalization"),
    "electrooxidative c-h": (4, "Electrochemical C-H", "C-H Functionalization"),
    "electrochemical cross-coupling": (4, "Electrochemical Cross-Coupling", "Cross-Coupling & C-C Formation"),
    "electrochemical cross coupling": (4, "Electrochemical Cross-Coupling", "Cross-Coupling & C-C Formation"),
    "electrochemical amination": (4, "Electrochemical Amination", "Cross-Coupling & C-C Formation"),
    "electrochemical arylation": (4, "Electrochemical Arylation", "Cross-Coupling & C-C Formation"),
    "electrochemical alkylation": (4, "Electrochemical Alkylation", "Cross-Coupling & C-C Formation"),
    "electrochemical annulation": (4, "Electrochemical Annulation", "Heterocycle Synthesis"),
    "electrochemical cyclization": (4, "Electrochemical Cyclization", "Heterocycle Synthesis"),
    "electrochemical dearomat": (4, "Electrochemical Dearomatization", "Anodic Oxidation"),
    "electrochemical carboxylation": (4, "Electrochemical Carboxylation", "Cathodic Reduction"),
    "electrocarboxylation": (4, "Electrochemical Carboxylation", "Cathodic Reduction"),
    "electrochemical fluorination": (4, "Electrochemical Fluorination", "Fluorination & Halogenation"),
    "electrochemical halogenation": (4, "Electrochemical Halogenation", "Fluorination & Halogenation"),
    "electrochemical chlorination": (4, "Electrochemical Halogenation", "Fluorination & Halogenation"),
    "electrochemical bromination": (4, "Electrochemical Halogenation", "Fluorination & Halogenation"),
    "electrochemical decarboxylat": (4, "Electrochemical Decarboxylation", "Decarboxylative & Radical Reactions"),
    "electrochemical hydrogenation of": (3, "Electrochemical Hydrogenation", "Cathodic Reduction"),
    "electrochemical deconstruct": (4, "Deconstructive Electrolysis", "Decarboxylative & Radical Reactions"),
    "electrochemical amidation": (4, "Electrochemical Amidation", "Cross-Coupling & C-C Formation"),
    "electrochemical oxygenation": (4, "Electrochemical Oxygenation", "Anodic Oxidation"),
    "electrochemical azidation": (4, "Electrochemical Azidation", "Decarboxylative & Radical Reactions"),
    "electrochemical thiolation": (4, "Electrochemical Thiolation", "Cross-Coupling & C-C Formation"),
    # --- mediated / indirect ---------------------------------------------
    "mediated electrolysis": (4, "Mediated Electrolysis", "Mediated & Indirect Electrolysis"),
    "indirect electrolysis": (4, "Indirect Electrolysis", "Mediated & Indirect Electrolysis"),
    "indirect electrochemical": (4, "Indirect Electrolysis", "Mediated & Indirect Electrolysis"),
    "electrochemical mediator": (4, "Redox Mediator", "Mediated & Indirect Electrolysis"),
    # --- electro + photo ---------------------------------------------------
    "electrophotocatal": (4, "Electrophotocatalysis", "Electrophotochemistry"),
    "electrophotochemical": (4, "Electrophotochemistry", "Electrophotochemistry"),
    "photoelectrochemical synthesis": (4, "Photoelectrosynthesis", "Electrophotochemistry"),
    "photoelectrosynthe": (4, "Photoelectrosynthesis", "Electrophotochemistry"),
    # --- asymmetric --------------------------------------------------------
    "asymmetric electrosynthesis": (4, "Asymmetric Electrosynthesis", "Asymmetric Electrosynthesis"),
    "enantioselective electro": (4, "Enantioselective Electrosynthesis", "Asymmetric Electrosynthesis"),
    "electrochemical asymmetric": (4, "Asymmetric Electrosynthesis", "Asymmetric Electrosynthesis"),
    # --- operating mode used synthetically --------------------------------
    "constant current electrolysis": (4, "Constant Current", "Cell Design & Electrodes"),
    "galvanostatic electrolysis": (4, "Galvanostatic", "Cell Design & Electrodes"),
    "controlled potential electrolysis": (4, "Controlled Potential", "Cell Design & Electrodes"),
    "potentiostatic electrolysis": (4, "Controlled Potential", "Cell Design & Electrodes"),
    "undivided cell": (4, "Undivided Cell", "Cell Design & Electrodes"),
    "divided cell": (3, "Divided Cell", "Cell Design & Electrodes"),
    "sacrificial anode": (4, "Sacrificial Anode", "Cell Design & Electrodes"),
    "electrochemical flow reactor": (4, "Electrochemical Flow Reactor", "Flow Electrosynthesis & Scale-up"),
    "electrochemical microreactor": (4, "Electrochemical Microreactor", "Flow Electrosynthesis & Scale-up"),
    "flow electrochemistry": (4, "Flow Electrochemistry", "Flow Electrosynthesis & Scale-up"),
    "electrochemical flow cell": (4, "Electrochemical Flow Cell", "Flow Electrosynthesis & Scale-up"),
}

# ---------------------------------------------------------------------------
# Support terms — hardware, mediators, methods, synthetic vocabulary
# ---------------------------------------------------------------------------
SUPPORT_TERMS: Dict[str, Tuple[int, str, str]] = {
    # cell hardware / electrodes
    "reticulated vitreous carbon": (4, "RVC Electrode", "Cell Design & Electrodes"),
    "boron-doped diamond": (3, "BDD Electrode", "Cell Design & Electrodes"),
    "glassy carbon electrode": (3, "Glassy Carbon", "Cell Design & Electrodes"),
    "graphite electrode": (3, "Graphite Electrode", "Cell Design & Electrodes"),
    "platinum electrode": (3, "Platinum Electrode", "Cell Design & Electrodes"),
    "nickel electrode": (2, "Nickel Electrode", "Cell Design & Electrodes"),
    "working electrode": (2, "Working Electrode", "Cell Design & Electrodes"),
    "counter electrode": (2, "Counter Electrode", "Cell Design & Electrodes"),
    "reference electrode": (2, "Reference Electrode", "Cell Design & Electrodes"),
    "supporting electrolyte": (4, "Supporting Electrolyte", "Cell Design & Electrodes"),
    "cell voltage": (2, "Cell Voltage", "Cell Design & Electrodes"),
    "electrolysis": (2, "Electrolysis", "General Electrosynthesis"),
    "electrolytic": (2, "Electrolytic", "General Electrosynthesis"),
    # mediators
    "tempo": (3, "TEMPO", "Mediated & Indirect Electrolysis"),
    "n-hydroxyphthalimide": (3, "NHPI", "Mediated & Indirect Electrolysis"),
    "redox mediator": (4, "Redox Mediator", "Mediated & Indirect Electrolysis"),
    "ferrocene": (2, "Ferrocene", "Mediated & Indirect Electrolysis"),
    "iodide mediat": (3, "Iodide Mediator", "Mediated & Indirect Electrolysis"),
    "triarylamine": (2, "Triarylamine", "Mediated & Indirect Electrolysis"),
    # electroanalytical / mechanistic
    "cyclic voltammetry": (3, "Cyclic Voltammetry", "Mechanism & Electroanalysis"),
    "cyclic voltammogram": (3, "Cyclic Voltammetry", "Mechanism & Electroanalysis"),
    "oxidation potential": (2, "Oxidation Potential", "Mechanism & Electroanalysis"),
    "reduction potential": (2, "Reduction Potential", "Mechanism & Electroanalysis"),
    "redox potential": (2, "Redox Potential", "Mechanism & Electroanalysis"),
    "single-electron transfer": (3, "Single-Electron Transfer", "Mechanism & Electroanalysis"),
    "single electron transfer": (3, "Single-Electron Transfer", "Mechanism & Electroanalysis"),
    "radical cation": (3, "Radical Cation", "Mechanism & Electroanalysis"),
    "radical anion": (3, "Radical Anion", "Mechanism & Electroanalysis"),
    "dft calculation": (2, "DFT", "Mechanism & Electroanalysis"),
    "reaction mechanism": (2, "Mechanism", "Mechanism & Electroanalysis"),
    # synthetic-organic vocabulary
    "c-h functionalization": (3, "C-H Functionalization", "C-H Functionalization"),
    "c–h functionalization": (3, "C-H Functionalization", "C-H Functionalization"),
    "c-h activation": (3, "C-H Activation", "C-H Functionalization"),
    "cross-coupling": (3, "Cross-Coupling", "Cross-Coupling & C-C Formation"),
    "cross coupling": (3, "Cross-Coupling", "Cross-Coupling & C-C Formation"),
    "c-c bond formation": (3, "C-C Bond Formation", "Cross-Coupling & C-C Formation"),
    "carbon-carbon bond": (2, "C-C Bond Formation", "Cross-Coupling & C-C Formation"),
    "radical": (2, "Radical Chemistry", "Decarboxylative & Radical Reactions"),
    "decarboxylative": (3, "Decarboxylative", "Decarboxylative & Radical Reactions"),
    "heterocycle": (3, "Heterocycles", "Heterocycle Synthesis"),
    "heterocyclic": (2, "Heterocycles", "Heterocycle Synthesis"),
    "indole": (2, "Indoles", "Heterocycle Synthesis"),
    "quinoline": (2, "Quinolines", "Heterocycle Synthesis"),
    "alkene": (2, "Alkenes", "General Electrosynthesis"),
    "alkyne": (2, "Alkynes", "General Electrosynthesis"),
    "arene": (2, "Arenes", "General Electrosynthesis"),
    "substrate scope": (3, "Substrate Scope", "General Electrosynthesis"),
    "functional group tolerance": (3, "FG Tolerance", "General Electrosynthesis"),
    "one-pot": (2, "One-Pot", "General Electrosynthesis"),
    "regioselectiv": (2, "Regioselectivity", "General Electrosynthesis"),
    "chemoselectiv": (2, "Chemoselectivity", "General Electrosynthesis"),
    "enantioselectiv": (3, "Enantioselectivity", "Asymmetric Electrosynthesis"),
    "diastereoselectiv": (2, "Diastereoselectivity", "Asymmetric Electrosynthesis"),
    "chiral catalyst": (3, "Chiral Catalyst", "Asymmetric Electrosynthesis"),
    # late-stage / medicinal / natural products
    "late-stage functionalization": (4, "Late-Stage Functionalization", "Late-Stage Functionalization & Medicinal Chemistry"),
    "late stage functionalization": (4, "Late-Stage Functionalization", "Late-Stage Functionalization & Medicinal Chemistry"),
    "drug molecule": (2, "Drug Molecules", "Late-Stage Functionalization & Medicinal Chemistry"),
    "active pharmaceutical ingredient": (3, "API", "Late-Stage Functionalization & Medicinal Chemistry"),
    "medicinal chemistry": (3, "Medicinal Chemistry", "Late-Stage Functionalization & Medicinal Chemistry"),
    "total synthesis": (4, "Total Synthesis", "Natural Product & Total Synthesis"),
    "natural product": (3, "Natural Products", "Natural Product & Total Synthesis"),
    "alkaloid": (2, "Alkaloids", "Natural Product & Total Synthesis"),
    # transition-metal catalysis in e-synthesis
    "nickel-catalyzed": (3, "Ni Catalysis", "Cross-Coupling & C-C Formation"),
    "nickel catalysis": (3, "Ni Catalysis", "Cross-Coupling & C-C Formation"),
    "palladium-catalyzed": (3, "Pd Catalysis", "Cross-Coupling & C-C Formation"),
    "cobalt-catalyzed": (3, "Co Catalysis", "Cross-Coupling & C-C Formation"),
    "copper-catalyzed": (3, "Cu Catalysis", "Cross-Coupling & C-C Formation"),
    "organocatalys": (2, "Organocatalysis", "General Electrosynthesis"),
    # scale-up / green
    "gram-scale": (3, "Gram-Scale", "Flow Electrosynthesis & Scale-up"),
    "gram scale": (3, "Gram-Scale", "Flow Electrosynthesis & Scale-up"),
    "kilogram": (3, "Kilogram-Scale", "Flow Electrosynthesis & Scale-up"),
    "scale-up": (3, "Scale-up", "Flow Electrosynthesis & Scale-up"),
    "continuous flow": (3, "Continuous Flow", "Flow Electrosynthesis & Scale-up"),
    "microreactor": (3, "Microreactor", "Flow Electrosynthesis & Scale-up"),
    "green chemistry": (3, "Green Chemistry", "Green & Sustainable Electrosynthesis"),
    "sustainable synthesis": (3, "Sustainable Synthesis", "Green & Sustainable Electrosynthesis"),
    "reagent-free": (3, "Reagent-Free", "Green & Sustainable Electrosynthesis"),
    "oxidant-free": (3, "Oxidant-Free", "Green & Sustainable Electrosynthesis"),
    "atom economy": (2, "Atom Economy", "Green & Sustainable Electrosynthesis"),
    "renewable electricity": (3, "Renewable Electricity", "Green & Sustainable Electrosynthesis"),
}

# ---------------------------------------------------------------------------
# Negative signals — electrochemistry that is NOT organic synthesis
# ---------------------------------------------------------------------------
NEGATIVE_TERMS: Dict[str, int] = {
    # batteries / energy storage
    "lithium-ion battery": 14,
    "lithium ion battery": 14,
    "sodium-ion battery": 14,
    "potassium-ion battery": 14,
    "lithium-sulfur": 14,
    "solid-state battery": 14,
    "battery": 10,
    "anode material": 12,
    "cathode material": 12,
    "supercapacitor": 14,
    "energy storage": 12,
    "energy density": 10,
    "power density": 8,
    "specific capacity": 12,
    "cycling stability": 8,
    "electrode material for": 10,
    "charge-discharge": 12,
    "charge/discharge": 12,
    # fuel cells / water splitting / energy electrocatalysis
    "fuel cell": 12,
    "proton exchange membrane": 10,
    "solid oxide": 10,
    "water splitting": 12,
    "hydrogen evolution reaction": 12,
    "oxygen evolution reaction": 12,
    "oxygen reduction reaction": 12,
    "overall water splitting": 14,
    "electrocatalyst for hydrogen": 14,
    "electrocatalyst for oxygen": 14,
    "co2 reduction reaction": 10,
    "electrochemical co2 reduction": 10,
    "nitrogen reduction reaction": 12,
    "ammonia electrosynthesis": 10,
    # corrosion / plating / metallurgy
    "corrosion": 12,
    "corrosion inhibitor": 14,
    "electroplating": 14,
    "electrodeposition of": 10,
    "electrowinning": 14,
    "anodizing": 12,
    "passivation film": 10,
    "galvanic corrosion": 14,
    # analytical / sensing
    "biosensor": 14,
    "electrochemical sensor": 12,
    "electrochemical detection": 12,
    "detection limit": 12,
    "limit of detection": 12,
    "stripping voltammetry": 12,
    "electrochemical determination": 14,
    "immunosensor": 14,
    "aptasensor": 14,
    # electrocatalytic small-molecule / feedstock conversion — says
    # "electrosynthesis" constantly but is energy catalysis, not synthesis
    "co2 electroreduction": 14,
    "co2 electrolysis": 14,
    "co2-to-": 14,
    "co2 to ethanol": 14,
    "co2 conversion": 12,
    "co2 utilization": 12,
    "urea electrosynthesis": 14,
    "urea synthesis": 12,
    "h2o2 electrosynthesis": 14,
    "hydrogen peroxide electrosynthesis": 14,
    "hydrogen peroxide production": 12,
    "ammonia synthesis": 12,
    "ammonia electrosynthesis": 14,
    "nitrate reduction": 14,
    "nitrate-to-ammonia": 14,
    "nitrogen fixation": 12,
    "methane electrosynthesis": 14,
    "syngas": 12,
    "formate production": 12,
    "acetate production": 12,
    "amino acid electrosynthesis": 12,
    "glycine electrosynthesis": 14,
    "sustainable aviation fuel": 14,
    "biomass-derived": 10,
    "biomass upgrading": 12,
    "chlorine evolution": 12,
    "active chlorine": 12,
    # heterogeneous-electrocatalyst materials design vocabulary
    "single-atom catalyst": 14,
    "single atom catalyst": 14,
    "dual-atom": 14,
    "single-atom site": 14,
    "heterostructure": 12,
    "oxygen vacanc": 10,
    "d-band center": 12,
    "adsorption energy": 12,
    "binding energy of": 10,
    "selectivity trade-off": 10,
    "mesoporous": 8,
    "nanosheet": 10,
    "nanoparticle catalyst": 8,
    "electrocatalytic activity": 8,
    "electrocatalyst design": 12,
    # analytical determination (voltammetry as a measurement, not synthesis)
    "voltammetric determination": 14,
    "differential pulse voltammetry": 12,
    "amperometric": 12,
    # advanced oxidation / effluent treatment
    "advanced oxidation process": 14,
    "advanced oxidation": 12,
    "dye removal": 14,
    "landfill leachate": 14,
    "water purification": 12,
    "water treatment": 12,
    # inorganic feedstock -> small molecule (CO2 / NOx / N2 / H2O2). These say
    # "electrosynthesis" but the product is not an organic target molecule.
    # "co2" is only lightly penalised: electrocarboxylation is genuine organic
    # electrosynthesis and carries its own PRIMARY term.
    "co2": 6,
    "carbon dioxide": 6,
    "from co2": 12,
    "from nitrate": 14,
    "nitrate": 10,
    "nitrite": 10,
    "hydrogen peroxide": 12,
    "h2o2": 10,
    "hydroxylamine": 8,
    "electrocatalytic oxidation": 8,
    "electrocatalysts": 8,
    "alloy": 8,
    # nanomaterial / film formation rather than molecular synthesis
    "quantum dot": 12,
    "oxide film": 12,
    "thin film": 8,
    "lignin": 12,
    # bioelectrochemical
    "bioanode": 14,
    "biohybrid": 12,
    "biocathode": 14,
    # environmental / bio / other
    "microbial electrosynthesis": 14,
    "microbial fuel cell": 14,
    "wastewater treatment": 12,
    "electrocoagulation": 14,
    "desalination": 12,
    "electrodialysis": 12,
    "capacitive deionization": 14,
    "degradation of pollutant": 10,
    "electro-fenton": 10,
    "solar cell": 12,
    "photovoltaic": 12,
    "electrochromic": 12,
    "dye-sensitized": 10,
}

# Journal-name fragments indicating a relevant venue (score bonus).
# Matches JACS, Org. Lett., Angew., Chem. Sci., Green Chem., ChemElectroChem,
# J. Org. Chem., Org. Process Res. Dev., Electrochim. Acta, etc.
CHEM_VENUE_HINTS = (
    "chem", "org", "synth", "catal", "electro", "green", "react",
    "angew", "jacs", "tetrahedron", "process", "sustain",
)
