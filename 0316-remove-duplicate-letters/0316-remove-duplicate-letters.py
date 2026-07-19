class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        st, seen = [], set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            while st and st[-1] > c and last[st[-1]] > i:
                seen.remove(st.pop())
            st.append(c)
            seen.add(c)

        return "".join(st)