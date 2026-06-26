class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        m = 2 * n + 3
        bit = [0] * m

        def add(i):
            while i < m:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        off = n + 2
        pre = 0
        ans = 0
        add(off)

        for x in nums:
            pre += 1 if x == target else -1
            idx = pre + off
            ans += query(idx - 1)
            add(idx)

        return ans