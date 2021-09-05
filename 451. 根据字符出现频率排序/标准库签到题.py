from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        res = ''
        while item := counter.most_common(1):
            ch, freq = item[0]
            counter.pop(ch)
            res += ch * freq

        return res
