class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        m = len(word2)
        last = [-1] * m

        i, j = len(word1) - 1, m - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        skip = True
        j = 0

        for i, c in enumerate(word1):
            if j == m:
                break

            if c == word2[j]:
                ans.append(i)
                j += 1
            elif skip and (j == m - 1 or i < last[j + 1]):
                ans.append(i)
                j += 1
                skip = False

        return ans if j == m else []