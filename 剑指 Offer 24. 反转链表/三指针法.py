class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head

        prev, now, last = None, head, head.next
        while last:
            now.next = prev
            prev, now, last = now, last, last.next

        now.next = prev
        return now
