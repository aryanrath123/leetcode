class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for a, b, d in roads:
            g[a].append((b, d))
            g[b].append((a, d))

        q = [1]
        vis = {1}
        ans = float('inf')

        while q:
            x = q.pop()
            for y, d in g[x]:
                ans = min(ans, d)
                if y not in vis:
                    vis.add(y)
                    q.append(y)

        return ans