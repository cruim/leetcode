from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        if nums:
            current_sum = best_sum = 0
            for index, i in enumerate(nums):
                if current_sum <= 0:
                    current_sum = i
                else:
                    current_sum += i
                if current_sum > best_sum:
                    best_sum = current_sum
            if best_sum <= 0:
                return max(nums)
            return best_sum
