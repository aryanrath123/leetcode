class Solution:
    def maxProduct(self, n: int) -> int:
        d = list(map(int, str(n)))
        d.sort(reverse=True)
        return d[0] * d[1]