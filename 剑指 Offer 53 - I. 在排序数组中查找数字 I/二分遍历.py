import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        ans = 0
        for i in range(idx, len(nums)):
            if nums[i] == target:
                ans += 1
            else:
                break

        return ans
