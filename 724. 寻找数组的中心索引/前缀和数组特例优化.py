from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        pre = [0]
        for i in nums:
            last = pre[-1]
            pre.append(last + i)

        last = pre[-1]

        for i in range(len(nums)):
            left = pre[i]
            right = last - pre[i + 1]
            if left == right:
                return i
        return -1
