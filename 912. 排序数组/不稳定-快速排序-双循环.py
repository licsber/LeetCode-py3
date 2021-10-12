import random
from typing import List


class Solution:
    def partition(self, nums, left, right):
        i, j = left, right
        v = nums[left]
        while True:
            i += 1
            if i != right:
                while nums[i] < v:
                    i += 1
                    if i == right:
                        break

            while nums[j] > v:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

    def quick_sort(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.quick_sort(nums, left, pivot - 1)
            self.quick_sort(nums, pivot + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        random.shuffle(nums)
        length = len(nums)
        self.quick_sort(nums, 0, length - 1)
        return nums
