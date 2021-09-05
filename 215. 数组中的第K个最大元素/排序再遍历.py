from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        res = last = nums[0]
        count = 1
        for num in nums:
            if last != num:
                count += 1
                if count == k:
                    res = num
                    break

        return res
