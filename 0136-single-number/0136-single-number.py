class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for n in nums:
            a = a^n
        return a
        