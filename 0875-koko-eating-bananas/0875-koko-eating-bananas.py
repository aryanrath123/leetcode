class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            hours = sum((p + m - 1) // m for p in piles)
            if hours <= h:
                r = m
            else:
                l = m + 1
        return l