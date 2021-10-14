from typing import List

from ListNode import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []

        ans = []

        def helper(now):
            if now.next:
                helper(now.next)

            ans.append(now.val)

        helper(head)
        return ans
