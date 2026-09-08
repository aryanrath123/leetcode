class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        for x in range(1000, n + 1):
            ans += (len(str(x)) - 1) // 3

        return ans