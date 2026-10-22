class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = nums[0]

        if all(nums[i] == (k + i) % n for i in range(n)):
            return min((n - k) % n, k + 2)

        k = (n - 1 - nums[0]) % n
        if all(nums[i] == (nums[0] - i) % n for i in range(n)):
            return min(k, n - k) + 1

        return -1