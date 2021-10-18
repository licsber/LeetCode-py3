from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional['TreeNode'], k: int) -> int:
        def gen(r):
            if r is not None:
                yield from gen(r.left)
                yield r.val
                yield from gen(r.right)

        ans = root.val
        it = gen(root)
        for _ in range(k):
            ans = next(it)

        return ans
