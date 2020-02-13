from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        first = cost[0]
        second = cost[1]
        for i in range(2, len(cost)):
            temp = min(first + cost[i], second + cost[i])
            first = second
            second = temp
        return min(first, second)
