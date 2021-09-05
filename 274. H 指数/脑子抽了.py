from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        citations.sort()
        h = l
        if citations[-1] == 0:
            return 0

        for i in range(1, l):
            if citations[i] < h:
                h = l - i
            else:
                if citations[i - 1] < h:
                    h -= 1
                break
        return h
