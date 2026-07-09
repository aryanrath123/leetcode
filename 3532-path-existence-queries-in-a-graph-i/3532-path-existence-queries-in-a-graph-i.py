class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        c = [0] * n
        for i in range(1, n):
            c[i] = c[i-1] + (nums[i] - nums[i-1] > maxDiff)
        
        return [c[u] == c[v] for u, v in queries]