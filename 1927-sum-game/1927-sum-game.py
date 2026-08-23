class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        q = 0

        for i, x in enumerate(num):
            if x == '?':
                q += 1 if i < n // 2 else -1
            else:
                diff += int(x) if i < n // 2 else -int(x)

        return q % 2 != 0 or diff != -9 * q // 2