from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        length = len(numbers)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] <= numbers[right]:
                right = mid
            elif numbers[mid] > numbers[left]:
                left = mid + 1
            else:
                right -= 1

        return numbers[left]
