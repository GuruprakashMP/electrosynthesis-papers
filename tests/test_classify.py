"""Tests for the core rule: electrochemistry used to make organic molecules."""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from ddc.classify import classify  # noqa: E402
from ddc.models import RawRecord  # noqa: E402


def record(title: str, abstract: str = "", journal: str = "") -> RawRecord:
    return RawRecord(title=title, abstract=abstract, journal=journal, source="test")


class TestClassify(unittest.TestCase):
    def test_accepts_baran_style_electrosynthesis(self):
        r = record(
            "Scalable electrochemical cross-coupling of aryl halides",
            "A nickel-catalyzed electrochemical cross-coupling run at constant "
            "current in an undivided cell with a sacrificial anode delivers the "
            "product on gram-scale with broad substrate scope.",
            journal="Journal of the American Chemical Society")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertGreaterEqual(verdict.score, 80)
        self.assertIn("Cross-Coupling & C-C Formation", verdict.categories)

    def test_accepts_anodic_oxidation(self):
        r = record(
            "Anodic oxidation of phenols for biaryl synthesis",
            "Preparative electrolysis at a boron-doped diamond electrode gives "
            "the coupled product; cyclic voltammetry supports a radical cation "
            "intermediate.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Anodic Oxidation", verdict.categories)

    def test_accepts_paired_electrolysis(self):
        r = record(
            "Paired electrolysis enables reagent-free oxidation and reduction",
            "Both electrodes are used productively in an undivided cell, "
            "improving atom economy of the electrosynthesis.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Paired Electrolysis", verdict.categories)

    def test_accepts_mediated_electrolysis(self):
        r = record(
            "TEMPO-mediated indirect electrolysis of alcohols",
            "A redox mediator shuttles electrons in this mediated electrolysis, "
            "avoiding stoichiometric oxidant.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Mediated & Indirect Electrolysis", verdict.categories)

    def test_accepts_electrophotochemistry(self):
        r = record(
            "Electrophotocatalysis for C–H functionalization of arenes",
            "Combining light and current, this electrophotochemical method "
            "achieves late-stage functionalization of drug molecules.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Electrophotochemistry", verdict.categories)

    def test_accepts_classic_kolbe(self):
        r = record(
            "Kolbe electrolysis of carboxylic acids at platinum electrodes",
            "Decarboxylative dimerization under constant current electrolysis.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Decarboxylative & Radical Reactions", verdict.categories)

    def test_accepts_flow_electrosynthesis(self):
        r = record(
            "Electrochemical microreactor for continuous electrosynthesis",
            "An electrochemical flow cell scales the anodic oxidation to "
            "gram-scale throughput.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Flow Electrosynthesis & Scale-up", verdict.categories)

    def test_rejects_lithium_battery(self):
        r = record(
            "High-capacity silicon anode material for lithium-ion batteries",
            "The electrode material shows excellent cycling stability and "
            "specific capacity over 500 charge-discharge cycles.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_water_splitting_electrocatalysis(self):
        r = record(
            "NiFe electrocatalyst for the oxygen evolution reaction",
            "A low overpotential for overall water splitting and stable "
            "hydrogen evolution reaction performance.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_electrochemical_sensor(self):
        r = record(
            "An electrochemical sensor for dopamine detection",
            "The modified glassy carbon electrode gives a low detection limit "
            "by differential pulse voltammetry.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_corrosion_study(self):
        r = record(
            "Corrosion inhibition of mild steel in acidic media",
            "Electrochemical impedance spectroscopy shows the corrosion "
            "inhibitor forms a passivation film.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_fuel_cell(self):
        r = record(
            "Pt/C catalyst for proton exchange membrane fuel cells",
            "Oxygen reduction reaction activity and power density were "
            "measured in a single fuel cell.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_plain_organic_synthesis(self):
        r = record(
            "Palladium-catalysed Suzuki coupling of aryl boronic acids",
            "A thermal cross-coupling with broad substrate scope and good "
            "functional group tolerance.")
        self.assertFalse(classify(r).accepted)

    def test_venue_boosts_score(self):
        base = record("Anodic oxidation of enol ethers",
                      "Preparative electrolysis in an undivided cell.")
        boosted = record("Anodic oxidation of enol ethers",
                         "Preparative electrolysis in an undivided cell.",
                         journal="Organic Letters")
        self.assertGreater(classify(boosted).score, classify(base).score)

    def test_empty_title_rejected(self):
        self.assertFalse(classify(record("")).accepted)

    def test_score_bounds(self):
        r = record(
            "Electrochemical C–H functionalization by paired electrolysis",
            "electrosynthesis anodic oxidation undivided cell supporting "
            "electrolyte TEMPO redox mediator substrate scope gram-scale "
            "late-stage functionalization cyclic voltammetry",
            journal="Journal of the American Chemical Society")
        verdict = classify(r)
        self.assertLessEqual(verdict.score, 100)
        self.assertGreaterEqual(verdict.score, 90)


if __name__ == "__main__":
    unittest.main()
