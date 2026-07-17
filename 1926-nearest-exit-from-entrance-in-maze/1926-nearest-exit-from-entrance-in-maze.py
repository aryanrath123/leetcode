class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            x, y, d = q.popleft()

            if (x != entrance[0] or y != entrance[1]) and (x == 0 or y == 0 or x == m - 1 or y == n - 1):
                return d

            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'
                    q.append((nx, ny, d + 1))

        return -1