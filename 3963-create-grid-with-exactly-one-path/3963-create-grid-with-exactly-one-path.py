class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        a = [['#']*n for _ in range(m)]
        for i in range(n): a[0][i]='.'
        for j in range(m): a[j][-1]='.'
        return [''.join(g) for g in a]