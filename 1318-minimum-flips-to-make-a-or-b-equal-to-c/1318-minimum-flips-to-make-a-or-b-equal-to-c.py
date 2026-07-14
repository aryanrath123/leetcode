class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            x, y, z = a & 1, b & 1, c & 1
            if z:
                if x == 0 and y == 0:
                    ans += 1
            else:
                ans += x + y
            a >>= 1
            b >>= 1
            c >>= 1
        return ans