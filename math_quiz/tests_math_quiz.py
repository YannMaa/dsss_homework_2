import unittest
from math_quiz import randomInt, randMathOperation, calc


class TestMathGame(unittest.TestCase):

    def test_randomInt(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomInt(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randMathOperation(self):
        # Test weather operations are only from the given list
        values = ['+', '-', '*']
        operation = randMathOperation()
        self.assertIn(operation,values)

    def test_calc(self):
            #check for some check cases
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6,4,'*','6 * 4', 24),
                (7,8,'-','7 - 8',-1),
                (4,1,'-','4 - 1',3),
                (5,2,'*','5 * 2',10)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                calc_problem, calc_answer = calc(num1,num2,operator)

                #check results
                assert calc_problem == expected_problem, f"Unexpected problem: {calc_problem}"
                assert calc_answer == expected_answer, f"Unexpected answer: {calc_answer}"

if __name__ == "__main__":
    unittest.main()
