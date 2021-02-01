from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) // 2
        A = set(A)
        for b in B:
            if (a := b + diff) in A:
                return [a, b]
