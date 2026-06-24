class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        o = head
        e = head.next
        h = e
        while e and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
        o.next = h
        return head