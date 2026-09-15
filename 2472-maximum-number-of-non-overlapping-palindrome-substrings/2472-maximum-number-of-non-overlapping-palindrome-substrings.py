class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(n):
            dp[i + 1] = dp[i]

            if i + 1 >= k and isPal(i - k + 1, i):
                dp[i + 1] = max(dp[i + 1], dp[i - k + 1] + 1)

            if i + 1 >= k + 1 and isPal(i - k, i):
                dp[i + 1] = max(dp[i + 1], dp[i - k] + 1)

        return dp[n]