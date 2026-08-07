from typing import List

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primes = [2, 3, 5, 7]
        need = []

        for p in primes:
            c = 0
            while t % p == 0:
                t //= p
                c += 1
            need.append(c)

        # Prime factor > 7 cannot come from digits 1-9
        if t > 1:
            return "-1"

        f = [
            (0,0,0,0), (0,0,0,0), (1,0,0,0),
            (0,1,0,0), (2,0,0,0), (0,0,1,0),
            (1,1,0,0), (0,0,0,1), (3,0,0,0),
            (0,2,0,0)
        ]

        A, B = need[0], need[1]

        # dp[a][b] = minimum digits needed for 2^a * 3^b
        dp = [[10**9] * (B + 1) for _ in range(A + 1)]
        dp[0][0] = 0

        for a in range(A + 1):
            for b in range(B + 1):
                if a == b == 0:
                    continue
                for d in (2, 3, 4, 6, 8, 9):
                    x, y = f[d][0], f[d][1]
                    dp[a][b] = min(
                        dp[a][b],
                        1 + dp[max(0, a-x)][max(0, b-y)]
                    )

        def required(r):
            return dp[r[0]][r[1]] + r[2] + r[3]

        def sub(r, d):
            return tuple(max(0, r[i] - f[d][i]) for i in range(4))

        def suffix(r, length):
            ans = []

            for pos in range(length):
                left = length - pos - 1

                for d in range(1, 10):
                    nr = sub(r, d)

                    if required(nr) <= left:
                        ans.append(str(d))
                        r = nr
                        break

            return ''.join(ans)

        n = len(num)
        rem = tuple(need)
        before = []

        # Scan until first zero
        for i, ch in enumerate(num):
            before.append(rem)

            if ch == '0':
                end = i
                break

            rem = sub(rem, int(ch))
        else:
            if required(rem) == 0:
                return num
            end = n - 1

        # Try increasing a digit from right to left
        for i in range(end, -1, -1):
            r = before[i]
            cur = int(num[i])

            for d in range(max(1, cur + 1), 10):
                nr = sub(r, d)
                left = n - i - 1

                if required(nr) <= left:
                    return num[:i] + str(d) + suffix(nr, left)

        # Need a longer number
        length = max(n + 1, required(tuple(need)))
        return suffix(tuple(need), length)