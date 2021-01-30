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
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        edges = []  # dis, from, to
        for i in range(m):
            for j in range(n):
                index = i * n + j
                if j > 0:
                    edges.append((max(grid[i][j], grid[i][j - 1]), index, index - 1))
                if i > 0:
                    edges.append((max(grid[i][j], grid[i - 1][j]), index, index - n))
        edges.sort()

        uf = UnionFind(m * n)
        ans = 0
        for d, f, t in edges:
            uf.unite(f, t)
            if uf.connected(0, uf.n - 1):
                ans = d
                break
        return ans
