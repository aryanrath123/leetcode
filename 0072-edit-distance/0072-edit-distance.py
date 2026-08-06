class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2) + 1))

        for i, a in enumerate(word1, 1):
            new = [i]
            for j, b in enumerate(word2, 1):
                new.append(dp[j-1] if a == b else 1 + min(dp[j], new[-1], dp[j-1]))
            dp = new

        return dp[-1]