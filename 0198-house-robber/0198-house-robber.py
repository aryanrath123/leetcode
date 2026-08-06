class Solution:
    def rob(self, nums):
        a = b = 0

        for x in nums:
            a, b = b, max(b, a + x)

        return b