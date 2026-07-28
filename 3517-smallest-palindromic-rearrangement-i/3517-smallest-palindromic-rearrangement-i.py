class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        cnt = Counter(s)
        half = []
        mid = ""

        for c in sorted(cnt):
            half.append(c * (cnt[c] // 2))
            if cnt[c] % 2:
                mid = c

        half = "".join(half)
        return half + mid + half[::-1]