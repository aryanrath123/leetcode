class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        from collections import deque

        m, n = len(classroom), len(classroom[0])
        pos = {}
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    pos[(i, j)] = k
                    k += 1

        target = (1 << k) - 1
        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        best[sr][sc][0] = energy

        q = deque([(sr, sc, 0, energy)])
        moves = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                if mask == target:
                    return moves

                if e == 0:
                    continue

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    nm = mask

                    if (nr, nc) in pos:
                        nm |= 1 << pos[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    if ne > best[nr][nc][nm]:
                        best[nr][nc][nm] = ne
                        q.append((nr, nc, nm, ne))

            moves += 1

        return -1