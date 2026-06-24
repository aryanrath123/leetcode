class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        while head:
            n = head.next
            head.next = p
            p = head
            head = n
        return p