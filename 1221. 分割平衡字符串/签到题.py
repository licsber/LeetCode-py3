class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = count = 0
        for ch in s:
            if ch == 'R':
                count += 1
            else:
                count -= 1

            if count == 0:
                ans += 1

        return ans
