class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            res, cur = set(), {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    part, i = parse(i + 1)
                elif expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1
                    continue
                else:
                    part, i = {expression[i]}, i + 1

                cur = {a + b for a in cur for b in part}

            return res | cur, i + 1

        return sorted(parse(0)[0])