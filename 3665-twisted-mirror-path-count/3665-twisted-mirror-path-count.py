class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        r = [[0] * n for _ in range(m)]
        d = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    r[i][j] = d[i][j] = 1
                elif grid[i][j] == 1:
                    r[i][j] = d[i + 1][j] if i + 1 < m else 0
                    d[i][j] = r[i][j + 1] if j + 1 < n else 0
                else:
                    right = r[i][j + 1] if j + 1 < n else 0
                    down = d[i + 1][j] if i + 1 < m else 0
                    r[i][j] = d[i][j] = (right + down) % mod

        return r[0][0]