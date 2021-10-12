import heapq
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        heapq.heapify(nums)
        nums = [heapq.heappop(nums) for _ in range(length)]
        return nums
