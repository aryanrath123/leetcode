class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        ans = 0

        for s, e in intervals[1:]:
            if s < end:
                ans += 1
            else:
                end = e

        return ans