class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        d = [[10**9] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    d[i][j] = 0
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < n and d[ni][nj] > d[i][j] + 1:
                    d[ni][nj] = d[i][j] + 1
                    q.append((ni, nj))

        def ok(x):
            if d[0][0] < x:
                return False
            vis = [[0] * n for _ in range(n)]
            q = deque([(0, 0)])
            vis[0][0] = 1

            while q:
                i, j = q.popleft()
                if i == n - 1 and j == n - 1:
                    return True
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and not vis[ni][nj] and d[ni][nj] >= x:
                        vis[ni][nj] = 1
                        q.append((ni, nj))
            return False

        l, r = 0, n * n
        while l < r:
            m = (l + r + 1) // 2
            if ok(m):
                l = m
            else:
                r = m - 1
        return l