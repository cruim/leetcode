class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            cur = [1,2]
        for i in range(3, n + 1):
            cur.append(cur[-1] + cur[-2])
        return cur[-1]
