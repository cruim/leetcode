class Solution:
    def longest_substring_length(self, s: str) -> int:
        best = ''
        for index, i in enumerate(s):
            cur = ''
            for j in s[index:]:
                if j not in cur:
                    cur += j
                    best = best if len(best) >= len(cur) else cur
                    continue
                else:
                    break
        return len(best)
