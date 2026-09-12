class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in a]

        import bisect

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, idx = a[i]
            j = bisect.bisect_right(starts, r)

            for k in range(1, 5):
                skip = dp[i + 1][k]
                take_score = w + dp[j][k - 1][0]
                take_indices = tuple(sorted((idx,) + dp[j][k - 1][1]))

                if take_score > skip[0] or (
                    take_score == skip[0] and take_indices < skip[1]
                ):
                    dp[i][k] = (take_score, take_indices)
                else:
                    dp[i][k] = skip

        return list(dp[0][4][1])