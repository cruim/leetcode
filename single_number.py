from collections import Counter
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]
