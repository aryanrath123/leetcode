class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = end = 0
        for l, r in intervals:
            if r > end:
                ans += 1
                end = r
        return ans