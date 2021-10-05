class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []

        s = s.replace('-', '')
        first = len(s) % k
        if first:
            ans.append(s[:first].upper())
            s = s[first:]

        for i in range(0, len(s), k):
            ans.append(s[i:i + k].upper())

        return '-'.join(ans)
