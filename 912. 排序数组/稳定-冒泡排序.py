from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(length - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums
