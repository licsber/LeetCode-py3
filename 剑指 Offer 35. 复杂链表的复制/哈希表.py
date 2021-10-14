from Node import Node


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        d = {}
        now = head
        while now:
            d[now] = Node(now.val)
            now = now.next

        now = head
        while now:
            if now.next:
                d[now].next = d[now.next]
            if now.random:
                d[now].random = d[now.random]
            now = now.next

        return d[head]
