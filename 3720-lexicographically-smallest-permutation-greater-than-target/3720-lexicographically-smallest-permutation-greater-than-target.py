class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = ""

        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            # Try making this position larger
            for c in range(x + 1, 26):
                if cnt[c]:
                    res = target[:i] + chr(c + ord('a'))
                    cnt[c] -= 1

                    for j in range(26):
                        res += chr(j + ord('a')) * cnt[j]

                    ans = res
                    cnt[c] += 1
                    break

            # Use target[i] if possible and continue
            if cnt[x] == 0:
                break

            cnt[x] -= 1

        return ans