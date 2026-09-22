class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = [[0] * k for _ in range(4 * n)]
        prod = [1] * (4 * n)

        def merge(p, a, b):
            prod[p] = prod[a] * prod[b] % k
            seg[p] = seg[a][:]
            for x in range(k):
                seg[p][prod[a] * x % k] += seg[b][x]

        def build(p, l, r):
            if l == r:
                prod[p] = nums[l] % k
                seg[p][prod[p]] = 1
                return
            m = (l + r) // 2
            build(p*2, l, m)
            build(p*2+1, m+1, r)
            merge(p, p*2, p*2+1)

        def update(p, l, r, i, v):
            if l == r:
                seg[p] = [0] * k
                prod[p] = v % k
                seg[p][prod[p]] = 1
                return
            m = (l + r) // 2
            if i <= m:
                update(p*2, l, m, i, v)
            else:
                update(p*2+1, m+1, r, i, v)
            merge(p, p*2, p*2+1)

        def query(p, l, r, s):
            if l >= s:
                return prod[p], seg[p]
            m = (l + r) // 2
            if s <= m:
                a = query(p*2, l, m, s)
                b = query(p*2+1, m+1, r, s)
                res = a[1][:]
                for x in range(k):
                    res[a[0] * x % k] += b[1][x]
                return a[0] * b[0] % k, res
            return query(p*2+1, m+1, r, s)

        build(1, 0, n-1)
        ans = []

        for i, v, s, x in queries:
            update(1, 0, n-1, i, v)
            ans.append(query(1, 0, n-1, s)[1][x])

        return ans