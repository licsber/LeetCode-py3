from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid - 1
                
        return l
