class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for x in nums:
            ndp = [0] * k
            v = x % k
            ndp[v] += 1

            for r in range(k):
                if dp[r]:
                    ndp[(r * v) % k] += dp[r]

            dp = ndp
            for r in range(k):
                ans[r] += dp[r]

        return ans