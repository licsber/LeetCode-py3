from typing import List

from ListNode import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next

        ans.reverse()
        return ans
