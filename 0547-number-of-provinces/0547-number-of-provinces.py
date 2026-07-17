class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n

        def dfs(i):
            vis[i] = True
            for j in range(n):
                if isConnected[i][j] and not vis[j]:
                    dfs(j)

        ans = 0
        for i in range(n):
            if not vis[i]:
                ans += 1
                dfs(i)

        return ans