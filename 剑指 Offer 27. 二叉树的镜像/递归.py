class Solution:
    def mirrorTree(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)

        return root
