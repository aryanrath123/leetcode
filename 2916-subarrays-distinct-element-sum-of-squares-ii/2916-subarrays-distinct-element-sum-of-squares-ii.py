class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        s, sq, lazy = [0]*(4*n), [0]*(4*n), [0]*(4*n)

        def apply(k, l, r, v):
            sq[k] = (sq[k] + 2*v*s[k] + (r-l+1)*v*v) % MOD
            s[k] = (s[k] + (r-l+1)*v) % MOD
            lazy[k] += v

        def push(k, l, r):
            if lazy[k] and l < r:
                m = (l+r)//2
                apply(2*k, l, m, lazy[k])
                apply(2*k+1, m+1, r, lazy[k])
                lazy[k] = 0

        def update(k, l, r, a, b):
            if a <= l and r <= b:
                apply(k, l, r, 1)
                return
            push(k, l, r)
            m = (l+r)//2
            if a <= m:
                update(2*k, l, m, a, b)
            if b > m:
                update(2*k+1, m+1, r, a, b)
            s[k] = (s[2*k] + s[2*k+1]) % MOD
            sq[k] = (sq[2*k] + sq[2*k+1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            update(1, 0, n-1, last.get(x, -1)+1, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans