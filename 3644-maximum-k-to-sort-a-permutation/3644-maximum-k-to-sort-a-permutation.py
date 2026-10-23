class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i, x in enumerate(nums):
            if i != x:
                ans &= x
        return ans if ans != -1 else 0