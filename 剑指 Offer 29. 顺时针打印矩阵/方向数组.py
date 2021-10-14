from collections import defaultdict
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans

        rows, cols = len(matrix), len(matrix[0])
        total = rows * cols

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        x = y = direction = 0
        vis = defaultdict(defaultdict)
        for idx in range(total):
            ans.append(matrix[x][y])
            vis[x][y] = True

            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= cols or ny >= rows or vis[nx][ny]:
                direction = (direction + 1) % 4

            x += dx[direction]
            y += dy[direction]

        return ans
