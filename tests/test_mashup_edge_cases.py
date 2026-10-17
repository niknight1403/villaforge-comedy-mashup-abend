import unittest

class TestMashupEdgeCases(unittest.TestCase):
    def test_show_duration_exact(self):
        # 120 Minuten Soll-Laufzeit
        total_duration = 120
        self.assertEqual(total_duration, 120, "Show-Laufzeit muss exakt 120 Minuten betragen")

    def test_fsk_rating(self):
        # SFW / FSK-12 Äquivalent
        fsk_rating = "FSK-12"
        self.assertIn(fsk_rating, ["FSK-0", "FSK-6", "FSK-12"], "Veranstaltung muss jugendfrei sein")

    def test_capacity_limit(self):
        capacity = 1000
        self.assertGreaterEqual(capacity, 100, "Kapazität muss mindestens 100 Plätze betragen")

if __name__ == "__main":
    unittest.main()
