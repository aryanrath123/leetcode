class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = {'a': 0, 'b': 0, 'c': 0}
        l = 0
        ans = 0
        n = len(s)
        for r in range(n):
            c[s[r]] += 1
            while c['a'] and c['b'] and c['c']:
                ans += n - r
                c[s[l]] -= 1
                l += 1
        return ans