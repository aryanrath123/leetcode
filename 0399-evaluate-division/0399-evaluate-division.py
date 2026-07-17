class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)

        for (a, b), v in zip(equations, values):
            g[a].append((b, v))
            g[b].append((a, 1 / v))

        ans = []

        for s, t in queries:
            if s not in g or t not in g:
                ans.append(-1.0)
                continue
            if s == t:
                ans.append(1.0)
                continue

            q = deque([(s, 1.0)])
            vis = {s}
            found = -1.0

            while q:
                x, val = q.popleft()
                if x == t:
                    found = val
                    break
                for y, w in g[x]:
                    if y not in vis:
                        vis.add(y)
                        q.append((y, val * w))

            ans.append(found)

        return ans