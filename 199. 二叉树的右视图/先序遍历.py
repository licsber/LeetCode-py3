from typing import List


class Solution:
    def rightSideView(self, root: 'TreeNode') -> List[int]:
        ans = []
        if not root:
            return ans

        count = 0

        def helper(node, level):
            nonlocal count

            if not node:
                return

            if count == level:
                ans.append(node.val)
                count += 1

            helper(node.right, level + 1)
            helper(node.left, level + 1)

        helper(root, 0)
        return ans
