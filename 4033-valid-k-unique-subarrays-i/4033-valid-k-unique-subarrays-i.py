class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        B = int(n ** 0.5)

        qs = sorted(
            [(l, r, i) for i, (l, r) in enumerate(queries)],
            key=lambda x: (x[0] // B, x[1] if (x[0] // B) % 2 == 0 else -x[1])
        )

        cnt = [0] * (max(nums) + 1)
        ans = [False] * len(queries)

        l, r = 0, -1
        distinct = odd = 0

        for ql, qr, idx in qs:

            while l > ql:
                l -= 1
                x = nums[l]
                if cnt[x] == 0:
                    distinct += 1
                odd += 1 if cnt[x] % 2 == 0 else -1
                cnt[x] += 1

            while r < qr:
                r += 1
                x = nums[r]
                if cnt[x] == 0:
                    distinct += 1
                odd += 1 if cnt[x] % 2 == 0 else -1
                cnt[x] += 1

            while l < ql:
                x = nums[l]
                cnt[x] -= 1
                odd += -1 if cnt[x] % 2 == 0 else 1
                if cnt[x] == 0:
                    distinct -= 1
                l += 1

            while r > qr:
                x = nums[r]
                cnt[x] -= 1
                odd += -1 if cnt[x] % 2 == 0 else 1
                if cnt[x] == 0:
                    distinct -= 1
                r -= 1

            ans[idx] = distinct == k and odd == 0

        return ans