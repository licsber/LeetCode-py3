import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        res = ' '
        d = collections.defaultdict(int)
        for ch in s:
            d[ch] += 1

        for k, v in d.items():
            if v == 1:
                res = k
                break

        return res
