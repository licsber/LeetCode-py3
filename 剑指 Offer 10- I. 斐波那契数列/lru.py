import functools


class Solution:
    @functools.lru_cache(None)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return (self.fib(n - 1) + self.fib(n - 2)) % 1000000007
