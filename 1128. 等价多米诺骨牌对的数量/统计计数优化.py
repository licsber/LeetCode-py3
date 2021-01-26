from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        counter = defaultdict(int)
        for i in dominoes:
            i.sort()
            num = i[0] * 10 + i[1]
            res += counter[num]
            counter[num] += 1
        return res
