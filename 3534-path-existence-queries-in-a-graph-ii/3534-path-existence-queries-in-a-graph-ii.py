class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        a = sorted((x, i) for i, x in enumerate(nums))
        pos = [0] * n
        for i, (_, j) in enumerate(a):
            pos[j] = i

        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and a[j + 1][0] - a[i][0] <= maxDiff:
                j += 1
            nxt[i] = j

        L = n.bit_length()
        up = [nxt]
        for _ in range(1, L):
            up.append([up[-1][up[-1][i]] for i in range(n)])

        ans = []
        for u, v in queries:
            l, r = sorted((pos[u], pos[v]))
            if l == r:
                ans.append(0)
                continue
            if nxt[l] == l:
                ans.append(-1)
                continue

            cur, d = l, 0
            for k in range(L - 1, -1, -1):
                if up[k][cur] < r and up[k][cur] != cur:
                    cur = up[k][cur]
                    d += 1 << k

            ans.append(d + 1 if nxt[cur] >= r else -1)

        return ans