class Solution:
    def solve1(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # https://leetcode.com/problems/find-the-distance-value-between-two-arrays/solutions/609472/java-binary-search-with-explanation-by-u-kyq2/
        arr2.sort()

        # 1. satisfies "NOT" in range
        # 2. use [a, b] form
        def isValid(n):
            l, r = 0, len(arr2)-1
            while l <= r:
                m = (l+r)//2
                if abs(n - arr2[m]) <= d:
                    return False
                elif arr2[m] < n:
                    l = m + 1
                else:
                    r = m - 1
            return True

        return sum(isValid(n) for n in arr1)

    def solve2(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # https://leetcode.com/problems/find-the-distance-value-between-two-arrays/solutions/6939070/binary-search-by-angielf-v1cm/
        arr2.sort()
        ans = 0
        for n in arr1:
            l = bisect_left(arr2, n - d)
            r = bisect_right(arr2, n + d)
            ans += 1 if l == r else 0
        return ans

    # prefered ...
    def solve3(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for n in arr1:
            mn = inf
            idx = bisect_left(arr2, n)
            if idx < len(arr2):
                mn = min(mn, arr2[idx] - n)
            if idx > 0:
                mn = min(mn, n - arr2[idx-1])
            res += 1 if mn > d else 0
        return res

    def mock(self, arr1: List[int], arr2: List[int], d: int) -> int:
        '''
        res = 0
        arr2.sort()
        for n in arr1:
            print(n, res)
            i = bisect_left(arr2, n)
            if i == 0:
                res += 1 if (arr2[i] - n) > d else 0
            elif i == len(arr2):
                res += 1 if (n - arr2[-1]) > d else 0
            else:
                res += 1 if min(arr2[i] - n, n - arr2[i-1]) > d else 0
            #print(n, res, i)
        return res
        '''
        res = 0
        arr2.sort()
        for n in arr1:
            idx = bisect_left(arr2, n)
            dist = inf
            if idx < len(arr2):
                dist = arr2[idx] - n
            if idx > 0:
                dist = min(dist, n - arr2[idx-1])
            res += 1 if dist > d else 0
        return res

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        '''
        # https://leetcode.com/problems/find-the-distance-value-between-two-arrays/solutions/1913945/problem-description-explained-in-simple-h3dj7/
        translation:
        Calculate the distance between arr1[i] and arr2[j] and find the number of elements in arr1 where it's distances are NOT LESS THAN or EQUAL TO d.
        '''
        #return self.solve3(arr1, arr2, d)
        return self.mock(arr1, arr2, d)