class Solution:
    def evaluate(self, s: str, d: List[List[str]]) -> str:
        return s.replace('(','{d[').replace(')',']}').format(d=defaultdict(lambda:'?',d))
        return re.sub(r'\((\w+)\)',lambda m,d=dict(d):d.get(m[1],'?'),s)