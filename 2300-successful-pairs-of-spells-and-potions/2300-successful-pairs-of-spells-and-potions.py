class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        ans = []

        for s in spells:
            l, r = 0, m
            while l < r:
                mid = (l + r) // 2
                if s * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1
            ans.append(m - l)

        return ans