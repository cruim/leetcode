from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for index, item in enumerate(nums):
            for i in nums[index+1::]:
                res = item + i
                if res == target:
                    return [nums.index(item), nums.index(i if item != i else i,index+1)]
