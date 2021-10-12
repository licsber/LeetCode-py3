from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            pre = i - 1
            now = nums[i]
            while pre >= 0 and nums[pre] > now:
                nums[pre + 1] = nums[pre]
                pre -= 1

            nums[pre + 1] = now

        return nums
