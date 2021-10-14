from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans

        top = left = 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while True:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return ans
