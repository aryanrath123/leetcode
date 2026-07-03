class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        ind = [0] * n
        mx = 0

        for u, v, w in edges:
            g[u].append((v, w))
            ind[v] += 1
            mx = max(mx, w)

        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                ind[v] -= 1
                if ind[v] == 0:
                    q.append(v)

        INF = 10**30

        def ok(x):
            dp = [INF] * n
            dp[0] = 0
            for u in topo:
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                if dp[u] == INF:
                    continue
                for v, w in g[u]:
                    if w < x:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dp[u] + w < dp[v]:
                        dp[v] = dp[u] + w
            return dp[-1] <= k

        if not ok(0):
            return -1

        l, r = 0, mx
        while l < r:
            m = (l + r + 1) // 2
            if ok(m):
                l = m
            else:
                r = m - 1
        return l