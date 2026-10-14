import unittest
from campusflow.reports import generate_report


class TestReports(unittest.TestCase):
    def test_empty_report(self):
        report = generate_report([])
        self.assertEqual(report["total"], 0)
        self.assertEqual(report["resolution_percentage"], 0)

    def test_report_counts(self):
        tickets = [
            {"status": "open", "priority": "high", "category": "Network"},
            {"status": "in_progress", "priority": "medium", "category": "Hardware"},
            {"status": "resolved", "priority": "low", "category": "Software"}
        ]

        report = generate_report(tickets)

        self.assertEqual(report["total"], 3)
        self.assertEqual(report["unresolved"], 2)
        self.assertEqual(report["resolved"], 1)
        self.assertAlmostEqual(report["resolution_percentage"], 33.33)

    def test_reopened_ticket_counts_as_open(self):
        tickets = [
            {"status": "open", "priority": "high", "category": "Network"}
        ]

        report = generate_report(tickets)

        self.assertEqual(report["by_status"]["open"], 1)
        self.assertEqual(report["resolved"], 0)


if __name__ == "__main__":
    unittest.main()
