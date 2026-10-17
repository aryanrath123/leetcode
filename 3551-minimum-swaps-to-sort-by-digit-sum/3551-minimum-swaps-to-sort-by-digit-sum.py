class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        a = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {v: i for i, v in enumerate(a)}
        p = [pos[x] for x in nums]
        vis = [0] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if vis[i] or p[i] == i:
                continue
            j, cnt = i, 0
            while not vis[j]:
                vis[j] = 1
                j = p[j]
                cnt += 1
            ans += cnt - 1

        return ans