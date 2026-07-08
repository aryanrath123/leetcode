class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(s)
        c = [0] * (n + 1)
        v = [0] * (n + 1)
        sm = [0] * (n + 1)
        p = [1] * (n + 1)

        for i, x in enumerate(s):
            d = int(x)
            c[i + 1] = c[i] + (d > 0)
            v[i + 1] = (v[i] * (10 if d else 1) + d) % mod
            sm[i + 1] = sm[i] + d
            p[i + 1] = p[i] * 10 % mod

        ans = []
        for l, r in queries:
            k = c[r + 1] - c[l]
            x = (v[r + 1] - v[l] * p[k]) % mod
            ans.append(x * (sm[r + 1] - sm[l]) % mod)

        return ans