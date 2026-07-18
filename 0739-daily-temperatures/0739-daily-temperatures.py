class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)

        return ans