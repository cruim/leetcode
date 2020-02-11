from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cur_list = [nums[0], max(nums[0], nums[1])]
        for index, i in enumerate(nums[2:], 2):
            cur_list.append(max(i + cur_list[index - 2], cur_list[index - 1]))
        return cur_list[-1]
