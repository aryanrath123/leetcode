class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        for a in text1:
            prev = 0
            for j, b in enumerate(text2, 1):
                temp = dp[j]
                if a == b:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[-1]