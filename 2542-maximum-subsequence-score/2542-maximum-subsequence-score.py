class Solution:
    def maxScore(self, nums1, nums2, k):
        a = sorted(zip(nums2, nums1), reverse=True)

        heap = []
        s = 0
        ans = 0

        for x, y in a:
            heapq.heappush(heap, y)
            s += y

            if len(heap) > k:
                s -= heapq.heappop(heap)

            if len(heap) == k:
                ans = max(ans, s * x)

        return ans