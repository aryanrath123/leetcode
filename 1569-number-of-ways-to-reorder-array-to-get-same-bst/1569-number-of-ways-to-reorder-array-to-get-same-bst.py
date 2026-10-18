class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        from math import comb

        def solve(a):
            if len(a) < 3:
                return 1
            left = [x for x in a if x < a[0]]
            right = [x for x in a if x > a[0]]
            return comb(len(left) + len(right), len(left)) * solve(left) * solve(right) % MOD

        return (solve(nums) - 1) % MOD