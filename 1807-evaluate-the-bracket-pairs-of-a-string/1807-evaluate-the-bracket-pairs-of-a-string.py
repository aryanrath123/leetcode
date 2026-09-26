class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        res = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]
                res.append(d.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1

        return ''.join(res)