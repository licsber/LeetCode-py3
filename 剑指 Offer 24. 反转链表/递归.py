class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
