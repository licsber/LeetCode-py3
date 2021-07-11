from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        citations.sort()
        for i, v in enumerate(citations):
            if l - i <= v:
                return l - i

        return 0
