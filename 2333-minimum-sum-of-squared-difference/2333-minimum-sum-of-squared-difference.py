class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(d) <= k:
            return 0

        l, r = 0, max(d)
        while l < r:
            m = (l + r) // 2
            if sum(max(x - m, 0) for x in d) <= k:
                r = m
            else:
                l = m + 1

        rem = k - sum(max(x - l, 0) for x in d)
        return sum(min(x, l) ** 2 for x in d) - rem * (2 * l - 1)