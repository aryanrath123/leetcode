class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        M = 200

        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [r[:] for r in dp]
            for g1 in range(M + 1):
                for g2 in range(M + 1):
                    if dp[g1][g2] == 0:
                        continue
                    v = dp[g1][g2]

                    ng1 = x if g1 == 0 else gcd(g1, x)
                    ndp[ng1][g2] = (ndp[ng1][g2] + v) % MOD

                    ng2 = x if g2 == 0 else gcd(g2, x)
                    ndp[g1][ng2] = (ndp[g1][ng2] + v) % MOD

            dp = ndp
        ans = 0
        for g in range(1, M + 1):
            ans = (ans + dp[g][g]) % MOD
        return ans