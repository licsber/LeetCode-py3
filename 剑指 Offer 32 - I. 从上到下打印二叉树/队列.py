from typing import List


class Solution:
    def levelOrder(self, root: 'TreeNode') -> List[int]:
        if not root:
            return []

        res = []

        q = [root]
        num = len(q)
        while q:
            while num:
                num -= 1
                node = q.pop(0)
                res.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            num = len(q)

        return res
