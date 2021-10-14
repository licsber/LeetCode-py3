from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans.extend(matrix[0])
            matrix = list(zip(*matrix[1:]))[::-1]
        return ans
