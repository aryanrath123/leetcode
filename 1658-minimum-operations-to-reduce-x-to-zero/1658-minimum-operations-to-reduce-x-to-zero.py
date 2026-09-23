class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        left = 0
        s = 0
        best = -1

        for right in range(len(nums)):
            s += nums[right]

            while s > target and left <= right:
                s -= nums[left]
                left += 1

            if s == target:
                best = max(best, right - left + 1)

        return len(nums) - best if best != -1 else -1