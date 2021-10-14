import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        return r - l
