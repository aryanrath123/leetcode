class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        size = [1] * n
        for u in reversed(order):
            if u:
                size[parent[u]] += size[u]

        tout = [tin[u] + size[u] - 1 for u in range(n)]

        log = n.bit_length()
        up = [parent]
        for _ in range(1, log):
            up.append([up[-1][up[-1][i]] for i in range(n)])

        pref = [0] * n
        chars = list(s)
        pref[0] = 1 << (ord(s[0]) - 97)

        for u in order[1:]:
            pref[u] = pref[parent[u]] ^ (1 << (ord(s[u]) - 97))

        bit = [0] * (n + 1)

        def add(i, x):
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def get(u):
            i, x = tin[u] + 1, 0
            while i:
                x ^= bit[i]
                i -= i & -i
            return x

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            d = depth[u] - depth[v]
            for k in range(log):
                if d >> k & 1:
                    u = up[k][u]

            if u == v:
                return u

            for k in range(log - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u, v = up[k][u], up[k][v]

            return parent[u]

        ans = []

        for q in queries:
            op, x, y = q.split()
            u = int(x)

            if op == "update":
                delta = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(y) - 97))
                chars[u] = y
                add(tin[u] + 1, delta)
                add(tout[u] + 2, delta)
            else:
                v = int(y)
                w = lca(u, v)
                mask = pref[u] ^ get(u) ^ pref[v] ^ get(v)
                mask ^= 1 << (ord(chars[w]) - 97)
                ans.append(mask.bit_count() <= 1)

        return ans