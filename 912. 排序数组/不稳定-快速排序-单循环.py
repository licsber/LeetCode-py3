import random
from typing import List


class Solution:
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if l < r:
            pivot = self.randomized_partition(nums, l, r)
            self.randomized_quicksort(nums, l, pivot - 1)
            self.randomized_quicksort(nums, pivot + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        self.randomized_quicksort(nums, 0, length - 1)
        return nums
