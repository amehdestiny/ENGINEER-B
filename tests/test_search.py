import unittest
from campusflow.search import search_tickets, sort_by_priority


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.tickets = [
            {"id": 1, "title": "Wi-Fi down", "category": "Network",
             "status": "open", "priority": "high"},
            {"id": 2, "title": "Laptop broken", "category": "Hardware",
             "status": "open", "priority": "critical"},
            {"id": 3, "title": "Wi-Fi fixed", "category": "Network",
             "status": "resolved", "priority": "low"}
        ]

    def test_case_insensitive_search(self):
        result = search_tickets(self.tickets, title="WI-FI")
        self.assertEqual([t["id"] for t in result], [1, 3])

    def test_combined_filters(self):
        result = search_tickets(
            self.tickets, "wi-fi", "Network", "open", "high"
        )
        self.assertEqual([t["id"] for t in result], [1])

    def test_no_matches(self):
        self.assertEqual(search_tickets(self.tickets, title="printer"), [])

    def test_sort_priority(self):
        result = sort_by_priority(self.tickets)
        self.assertEqual([t["id"] for t in result], [2, 1, 3])


if __name__ == "__main__":
    unittest.main()
