import collections
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1

        keys = sorted(counter.keys())
        return [key for key in keys for _ in range(counter[key])]
