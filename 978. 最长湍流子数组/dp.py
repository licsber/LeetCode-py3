from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = up = down = 1
        L = len(arr)
        for i in range(1, L):
            if arr[i - 1] < arr[i]:
                up = down + 1
                down = 1
            elif arr[i - 1] > arr[i]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            res = max(res, max(up, down))
        return res
