from typing import List


class Solution:
    def levelOrder(self, root: 'TreeNode') -> List[List[int]]:
        res = []

        def walk(node, level):
            if not node:
                return

            if len(res) == level:
                res.append([])

            if level & 1:
                res[level].insert(0, node.val)
            else:
                res[level].append(node.val)

            walk(node.left, level + 1)
            walk(node.right, level + 1)

        walk(root, 0)
        return res
