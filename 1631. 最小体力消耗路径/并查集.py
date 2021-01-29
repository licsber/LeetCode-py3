from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n
        self.setCount = n  # 当前连通分量数目

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False

        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        edges = []  # dis, x, y

        for i in range(m):
            for j in range(n):
                index = i * n + j
                if i > 0:
                    edges.append((abs(heights[i][j] - heights[i - 1][j]), index - n, index))
                if j > 0:
                    edges.append((abs(heights[i][j] - heights[i][j - 1]), index - 1, index))
        edges.sort()

        uf = UnionFind(m * n)
        ans = 0
        for dis, x, y in edges:
            uf.unite(x, y)
            if uf.connected(0, uf.n - 1):
                ans = dis
                break

        return ans
