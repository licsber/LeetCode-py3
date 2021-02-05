from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        L = len(cardPoints)
        left, right = 0, L - k
        res = now = sum(cardPoints[left:right])

        while right < L:
            now = now - cardPoints[left] + cardPoints[right]
            res = min(res, now)
            left += 1
            right += 1
        return sum(cardPoints) - res
