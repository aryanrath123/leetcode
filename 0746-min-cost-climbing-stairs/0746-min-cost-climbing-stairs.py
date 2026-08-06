class Solution:
    def minCostClimbingStairs(self, cost):
        a, b = 0, 0
        for x in cost:
            a, b = b, min(a, b) + x
        return min(a, b)