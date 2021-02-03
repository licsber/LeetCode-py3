from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        last = ans = sum(nums[:k])
        l = len(nums)
        for i in range(1, l - k + 1):
            last -= nums[i - 1]
            last += nums[i + k - 1]
            ans = max(ans, last)
        return ans / k
