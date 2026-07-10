class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def fun(x, a):
            if len(a) == k:
                if sum(a) == n:
                    ans.append(a[:])
                return

            for i in range(x, 10):
                fun(i + 1, a + [i])

        fun(1, [])
        return ans