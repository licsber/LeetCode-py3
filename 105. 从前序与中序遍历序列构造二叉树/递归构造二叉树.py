from typing import List


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# noinspection PyUnresolvedReferences
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        roots = {inorder[i]: i for i in range(len(inorder))}

        def build(preorder, inorder, pl, pr, il):
            if pl > pr:
                return None
            now = TreeNode(preorder[pl])
            proot = roots[now.val]
            nleft = proot - il

            now.left = build(preorder, inorder, pl + 1, pl + nleft, il)
            now.right = build(preorder, inorder, pl + nleft + 1, pr, proot + 1)
            return now

        return build(preorder, inorder, 0, len(preorder) - 1, 0)
