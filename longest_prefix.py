from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        min_word = min(strs, key=len)
        min_len = len(min_word)
        for _ in range(min_len):
            for j in strs:
                if j[:min_len] != min_word:
                    min_word = min_word[:min_len - 1]
                    break
                else:
                    continue
            if len(min_word) == min_len:
                return min_word
            else:
                min_len -= 1
