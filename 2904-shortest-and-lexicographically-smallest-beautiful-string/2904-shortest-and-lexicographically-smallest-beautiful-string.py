class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        min_len = float("inf")

        for i in range(len(s)):
            ones = 0

            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    cur = s[i:j + 1]

                    if len(cur) < min_len:
                        min_len = len(cur)
                        ans = cur
                    elif len(cur) == min_len and cur < ans:
                        ans = cur

                    break

                if ones > k:
                    break

        return ans