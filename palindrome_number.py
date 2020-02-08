class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        length = len(num)
        count = -1
        for i in range(int(length / 2)):
            if num[i] != num[count]:
                return False
            count -= 1
        return True
