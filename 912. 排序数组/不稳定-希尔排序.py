from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        gap = 1
        while gap < length / 3:
            gap = gap * 3 + 1

        while gap > 0:
            for i in range(gap, length):
                tmp = nums[i]
                j = i - gap
                while j >= 0 and nums[j] > tmp:
                    nums[j + gap] = nums[j]
                    j -= gap

                nums[j + gap] = tmp

            gap = gap // 3

        return nums
