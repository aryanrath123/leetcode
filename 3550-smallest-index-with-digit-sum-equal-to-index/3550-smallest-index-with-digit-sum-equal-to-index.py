class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if sum(map(int, str(n))) == i:
                return i
        return -1