class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        r = [0]*(n+1)
        for i in range(1, n+1):
            r[i] = r[i>>1] + (i & 1)
        return r

        