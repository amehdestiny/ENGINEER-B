import unittest
from campusflow.understanding_check import QUESTIONS, calculate_score


class TestUnderstanding(unittest.TestCase):
    def test_all_correct(self):
        answers = [question[2] for question in QUESTIONS]
        self.assertEqual(calculate_score(answers), 6)

    def test_all_wrong(self):
        answers = ["A" if q[2] != "A" else "B" for q in QUESTIONS]
        self.assertEqual(calculate_score(answers), 0)

    def test_partial_score(self):
        answers = [q[2] for q in QUESTIONS]
        answers[0] = "A" if answers[0] != "A" else "B"
        self.assertEqual(calculate_score(answers), 5)


if __name__ == "__main__":
    unittest.main()
