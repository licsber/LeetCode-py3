from typing import List


class Solution:
    def merge(self, left, right):
        res = []
        while left and right:
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))

        while left:
            res.append(left.pop(0))
        while right:
            res.append(right.pop(0))

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length < 2:
            return nums

        mid = length // 2
        left, right = nums[:mid], nums[mid:]
        return self.merge(self.sortArray(left), self.sortArray(right))
