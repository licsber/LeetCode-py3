from typing import List


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# noinspection PyUnresolvedReferences
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = preorder.pop(0)
        node = TreeNode(root)
        index = inorder.index(root)

        node.left = self.buildTree(preorder[:index], inorder[:index])
        node.right = self.buildTree(preorder[index:], inorder[index + 1:])
        return node
