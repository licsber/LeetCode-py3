from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        pre = []
        for i in nums:
            last = pre[-1] if pre else 0
            pre.append(last + i)

        last = pre[-1]
        if last - pre[0] == 0:
            return 0

        for i in range(1, len(pre)):
            left = pre[i - 1]
            right = last - pre[i]
            if left == right:
                return i
        return -1
