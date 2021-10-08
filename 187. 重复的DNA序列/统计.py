from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(int)
        for sub in range(len(s) - 10 + 1):
            sub = s[sub:sub + 10]
            d[sub] += 1

        res = []
        for i, v in d.items():
            if v > 1:
                res.append(i)

        return res
