class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            ok = True
            for i in range(0, n, k):
                b = nums[i:i + k]
                p = 0

                for j in range(k - 1):
                    if b[j] > b[j + 1]:
                        if p:
                            ok = False
                            break
                        p = j + 1

                if not ok or b[p:] + b[:p] != s[i:i + k]:
                    ok = False
                    break

            if ok:
                ans += k

        return ans