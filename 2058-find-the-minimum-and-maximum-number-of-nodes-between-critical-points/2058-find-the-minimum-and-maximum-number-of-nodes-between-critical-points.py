class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, cur = head, head.next
        first = last = -1
        mn = float('inf')
        pos = 1

        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or \
               (cur.val < prev.val and cur.val < cur.next.val):
                if first == -1:
                    first = pos
                else:
                    mn = min(mn, pos - last)
                last = pos
            prev, cur = cur, cur.next
            pos += 1

        return [-1, -1] if first == last else [mn, last - first]