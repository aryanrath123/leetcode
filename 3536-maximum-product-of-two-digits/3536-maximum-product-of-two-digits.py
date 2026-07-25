class Solution:
    def maxProduct(self, n: int) -> int:
        a = b = 0
        while n:
            d = n % 10
            if d >= a:
                b = a
                a = d
            elif d > b:
                b = d
            n //= 10
        return a * b