class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 31

        for x in nums:
            for b in range(31):
                cnt[b] += (x >> b) & 1

        ans = 0
        for _ in range(k):
            x = 0
            for b in range(31):
                if cnt[b]:
                    cnt[b] -= 1
                    x |= 1 << b
            ans = (ans + x * x) % mod

        return ans