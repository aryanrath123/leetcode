class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        ans = 1
        end = points[0][1]

        for s, e in points[1:]:
            if s > end:
                ans += 1
                end = e

        return ans