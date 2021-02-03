from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k
        last = ans = sum(nums[:k])

        l = len(nums)
        while right < l:
            last += nums[right]
            last -= nums[left]
            ans = max(ans, last)
            left += 1
            right += 1
        return ans / k
