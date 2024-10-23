import unittest
from unittest.mock import patch
from functions import ask_question

class TestAskQuestion(unittest.TestCase):
    def setUp(self):
        # Sample question data
        self.row_correct = ["What is 2 + 2?", "3", "4", "5", "6", "B"]
        self.row_incorrect = ["What is the color of the sky?", "Red", "Green", "Blue", "Yellow", "C"]

    @patch('builtins.input', side_effect=['B'])
    def test_correct_answer(self, mock_input):
        # Test case for when the correct answer is given
        result = ask_question(self.row_correct)
        self.assertEqual(result, 1)  # Expect 1 point for a correct answer

    @patch('builtins.input', side_effect=['A'])
    def test_incorrect_answer(self, mock_input):
        # Test case for when an incorrect answer is given
        result = ask_question(self.row_incorrect)
        self.assertEqual(result, 0)  # Expect 0 points for an incorrect answer

    @patch('builtins.input', side_effect=['E', 'B'])
    def test_invalid_then_correct_answer(self, mock_input):
        # Test case where the user first enters an invalid answer, then the correct one
        result = ask_question(self.row_correct)
        self.assertEqual(result, 1)  # Expect 1 point for a correct answer after invalid input

    @patch('builtins.input', side_effect=['F', 'G', 'A'])
    def test_multiple_invalid_then_incorrect_answer(self, mock_input):
        # Test case where the user enters multiple invalid answers, then an incorrect one
        result = ask_question(self.row_correct)
        self.assertEqual(result, 0)  # Expect 0 points for an incorrect answer after invalid inputs

# Run the tests
if __name__ == "__main__":
    unittest.main()