from collections import defaultdict
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] == 2:
                return num
