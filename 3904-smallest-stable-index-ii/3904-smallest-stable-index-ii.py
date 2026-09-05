class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suf = nums[:]
        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i], suf[i+1])
        m = 0
        for i in range(n):
            m = max(m, nums[i])
            if m-suf[i] <= k:
                return i
        return -1
        