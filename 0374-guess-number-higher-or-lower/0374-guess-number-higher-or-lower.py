class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            x = guess(m)
            
            if x == 0:
                return m
            if x == 1:
                l = m + 1
            else:
                r = m - 1