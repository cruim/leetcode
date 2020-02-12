from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        start = prices[0]
        best = 0
        for index, i in enumerate(prices[1:], 1):
            start = min(start, i)
            best = max(best, i - start)
        return best
