class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r, d = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            x, y = r.popleft(), d.popleft()
            if x < y:
                r.append(x + n)
            else:
                d.append(y + n)

        return "Radiant" if r else "Dire"