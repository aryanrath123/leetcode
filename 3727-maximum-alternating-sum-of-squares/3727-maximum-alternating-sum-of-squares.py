class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted(x * x for x in nums)
        return sum(a[len(a)//2:]) - sum(a[:len(a)//2])