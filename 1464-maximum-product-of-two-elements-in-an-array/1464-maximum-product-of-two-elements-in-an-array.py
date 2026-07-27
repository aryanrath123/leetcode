class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = 0
        for x in nums:
            if x > a:
                b = a
                a = x
            elif x > b:
                b = x
        return (a - 1) * (b - 1)