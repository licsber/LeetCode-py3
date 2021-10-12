from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            minIdx = i
            for j in range(i + 1, length):
                if nums[j] < nums[minIdx]:
                    minIdx = j

            nums[i], nums[minIdx] = nums[minIdx], nums[i]

        return nums
