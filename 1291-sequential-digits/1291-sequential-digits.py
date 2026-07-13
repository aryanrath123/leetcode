class Solution:
    def sequentialDigits(self, low: int, high: int):
        s = "123456789"
        a = []
        for l in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - l):
                n = int(s[i:i + l])
                if low <= n <= high:
                    a.append(n)
        return a