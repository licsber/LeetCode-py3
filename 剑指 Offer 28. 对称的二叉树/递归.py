class Solution:
    def isSymmetric(self, root: 'TreeNode') -> bool:
        if not root:
            return True

        def helper(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            return a.val == b.val and \
                   helper(a.left, b.right) and \
                   helper(a.right, b.left)

        return helper(root.left, root.right)
