import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stock_index = 0
        prev_price = prices[stock_index]
        while True:
            stock_index += 1
            try:
                next_price = prices[stock_index]
            except IndexError:
                break
            diff = next_price - prev_price
            if diff > 0:
                profit += diff
            prev_price = next_price
        return profit


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution_instance = Solution()

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.solution_instance

    def test1(self):
        input = [7, 1, 5, 3, 6, 4]
        output = 7
        result = self.solution_instance.maxProfit(input)
        self.assertEqual(output, result)

    def test2(self):
        input = [1, 2, 3, 4, 5]
        output = 4
        result = self.solution_instance.maxProfit(input)
        self.assertEqual(result, output)

    def test3(self):
        input = [7, 6, 4, 3, 1]
        output = 0
        result = self.solution_instance.maxProfit(input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
