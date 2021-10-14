class Solution:
    def numWays(self, n: int) -> int:
        a = b = 1
        for i in range(2, n + 1):
            b += a
            a = b - a
            b %= 1000000007
        return b
