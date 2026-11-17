"""Routing and citation behavior that the skill instructions rely on."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "lib"))
import cdpi

ROUTES = json.loads((ROOT / "data/routes.json").read_text())


def top(request):
    commands, blocks = cdpi.score_route(request, ROUTES)
    return (commands[0][1] if commands else ROUTES["default"]), [b for _, b in blocks]


class RouteTests(unittest.TestCase):
    def test_requests_reach_the_intended_playbook(self):
        cases = {
            "review this PR that adds a central postgres for all user records": "lens",
            "we have a legacy REST service, should we rewrite it": "plus-one",
            "design the protocol schema for our cross-chain messages": "spec-first",
            "is my oracle aggregator really infrastructure others can build on": "rails-check",
            "split our everything app into modules": "unbundle",
            "what is the difference between DPG and DPI": "explain",
        }
        for request, expected in cases.items():
            with self.subTest(request=request):
                self.assertEqual(top(request)[0], expected)

    def test_concerns_are_detected_from_software_terms(self):
        self.assertIn("registry", top("a central database for every record")[1])
        self.assertIn("consent", top("how should we store PII and consent")[1])
        self.assertIn("signing", top("sign the attestation with our keys")[1])

    def test_unmatched_request_falls_back_to_lens(self):
        self.assertEqual(top("zzz qqq")[0], "lens")

    def test_every_card_exists(self):
        for name, spec in ROUTES["commands"].items():
            self.assertTrue((ROOT / "reference" / spec["card"]).is_file(), name)


class CitationTests(unittest.TestCase):
    def test_gitbook_paths_map_to_live_urls(self):
        self.assertEqual(cdpi.url_for("docs", "the-dpi-wiki/is-my-system-a-dpi/README.md"),
                         "https://docs.cdpi.dev/the-dpi-wiki/is-my-system-a-dpi")
        self.assertEqual(cdpi.url_for("docs", "dpi/digital-payment-networks/interoperable-qr-code.md"),
                         "https://docs.cdpi.dev/technical-notes/digital-payment-networks/interoperable-qr-code")

    def test_markup_is_stripped(self):
        text = cdpi.clean("---\ndescription: x\n---\n# T\n{% hint %}a&#x20;<mark>b</mark>{% endhint %}")
        self.assertEqual(text, "# T\na b")

    @unittest.skipUnless(cdpi.local_ref("docs"), "sources not synced")
    def test_every_routed_page_is_in_the_pinned_sources(self):
        for name, block in ROUTES["blocks"].items():
            for page in block["docs"]:
                self.assertTrue((cdpi.source_dir("docs") / page).is_file(), f"{name}: {page}")
            for skill in block.get("skills", []):
                self.assertTrue((cdpi.source_dir("ai-skills") / f"skills/{skill}.md").is_file(), f"{name}: {skill}")


if __name__ == "__main__":
    unittest.main()
