class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = b = c = -10**9
        x = y = 10**9
        for n in nums:
            if n >= a:
                c, b, a = b, a, n
            elif n >= b:
                c, b = b, n
            elif n > c:
                c = n

            if n <= x:
                y, x = x, n
            elif n < y:
                y = n
        return max(a * b * c, a * x * y)