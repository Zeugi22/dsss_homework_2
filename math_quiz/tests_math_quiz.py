import unittest
from math_quiz import create_random_number, choose_operation, generate_problem


class TestMathGame(unittest.TestCase):

    def test_create_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = create_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operation(self):
        for _ in range(1000):
            op = choose_operation()
            self.assertIn(op, ('+', '-', '*'))
    
    def test_generate_problem(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 6, '*', '10 * 6', 60),
            (1, 1, '-', '1 - 1', 0),
            (5, 2, '-', '5 - 2', 3),
            (2, 5, '-', '2 - 5', -3),
            (100, 100, '+', '100 + 100', 200),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem(num1, num2, operator)
            self.assertEqual((expected_problem, expected_answer), (problem, answer))

if __name__ == "__main__":
    unittest.main()
