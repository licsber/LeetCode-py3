from bisect import bisect_left
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        mid = k // 2
        if k % 2 == 0:
            def median(x):
                return (x[mid - 1] + x[mid]) / 2
        else:
            def median(x):
                return x[mid]

        win = nums[:k]
        win.sort()
        res = [median(win)]

        l = len(nums)
        for i in range(0, l - k):
            right = nums[i + k]
            idx = bisect_left(win, right)
            win.insert(idx, right)

            left = nums[i]
            idx = bisect_left(win, left)
            del win[idx]

            res.append(median(win))
        return res
