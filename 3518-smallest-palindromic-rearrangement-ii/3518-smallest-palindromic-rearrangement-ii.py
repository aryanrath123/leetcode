from collections import Counter
from math import gcd

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        half = [0] * 26
        mid = ""

        for ch in freq:
            if freq[ch] % 2:
                mid = ch
            half[ord(ch) - 97] = freq[ch] // 2

        CAP = k

        def comb(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                a = n - r + i
                b = i
                g = gcd(a, b)
                a //= g
                b //= g
                g = gcd(res, b)
                res //= g
                b //= g
                res *= a
                if res > CAP:
                    return CAP + 1
                res //= b
            return res

        def count(cnt):
            rem = sum(cnt)
            res = 1
            for c in cnt:
                if c:
                    res *= comb(rem, c)
                    if res > CAP:
                        return CAP + 1
                    rem -= c
            return res

        if count(half) < k:
            return ""

        left = []
        for _ in range(sum(half)):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                x = count(half)
                if x >= k:
                    left.append(chr(i + 97))
                    break
                k -= x
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]