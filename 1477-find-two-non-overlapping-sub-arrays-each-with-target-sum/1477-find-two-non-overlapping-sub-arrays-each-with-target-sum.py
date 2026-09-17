class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = float('inf')
        ans = float('inf')
        left = 0
        s = 0
        dp = [float('inf')] * n

        for right in range(n):
            s += arr[right]

            while s > target:
                s -= arr[left]
                left += 1

            if s == target:
                length = right - left + 1
                if left > 0 and dp[left - 1] != float('inf'):
                    ans = min(ans, length + dp[left - 1])
                best = min(best, length)

            dp[right] = best

        return -1 if ans == float('inf') else ans