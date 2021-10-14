from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1 if matrix else 0
        while row < len(matrix) and col >= 0:
            now = matrix[row][col]
            if now == target:
                return True
            elif now < target:
                row += 1
            else:
                col -= 1

        return False
