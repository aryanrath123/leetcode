class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for c in s:
            for j in range(len(t) - 1, -1, -1):
                if c == t[j]:
                    dp[j + 1] += dp[j]

        return dp[-1]