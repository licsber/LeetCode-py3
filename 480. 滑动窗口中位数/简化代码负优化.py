import bisect
from statistics import median
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        win = nums[:k]
        win.sort()
        res = [median(win)]

        l = len(nums)
        for i in range(0, l - k):
            right = nums[i + k]
            bisect.insort(win, right)

            left = nums[i]
            idx = bisect.bisect_left(win, left)
            del win[idx]

            res.append(median(win))
        return res
