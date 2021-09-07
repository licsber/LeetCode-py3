from typing import Optional

from ListNode import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        count = 1
        p = head
        while p.next:
            p = p.next
            count += 1

        k %= count
        if k == 0:
            return head

        p.next = head
        p = head
        for _ in range(count - k - 1):
            p = p.next

        head = p.next
        p.next = None
        return head
