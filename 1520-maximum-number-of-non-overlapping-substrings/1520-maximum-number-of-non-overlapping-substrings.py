class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [len(s)] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            x = ord(c) - 97
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for c in range(26):
            if first[c] == len(s):
                continue

            l, r = first[c], last[c]
            i = l
            ok = True

            while i <= r:
                x = ord(s[i]) - 97
                if first[x] < l:
                    ok = False
                    break
                r = max(r, last[x])
                i += 1

            if ok:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans