from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = True
        L = len(nums)
        for i in range(1, L):
            if nums[i - 1] <= nums[i]:
                continue
            if not flag:
                return False
            # once
            flag = False
            if i != 1 and nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1]
        return True
