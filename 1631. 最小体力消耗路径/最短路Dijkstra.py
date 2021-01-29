import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        p = [(0, 0, 0)]  # dis, x, y
        dis = [0.] + [float('inf')] * (m * n - 1)
        vis = set()

        while p:
            d, x, y = heapq.heappop(p)
            index = x * n + y
            if index in vis:
                continue
            if (x, y) == (m - 1, n - 1):
                break

            vis.add(index)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    index = nx * n + ny
                    if dis[index] > (now := max(d, abs(heights[x][y] - heights[nx][ny]))):
                        dis[index] = now
                        heapq.heappush(p, (now, nx, ny))
        return int(dis[-1])
