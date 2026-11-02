class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m = nums[len(nums) // 2]
        return sum(abs(x - m) for x in nums)