class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
        left, right = 0, 0
        now = 0

        l = len(s)
        while right < l:
            now += cost[right]
            if now > maxCost:
                now -= cost[left]
                left += 1
            right += 1
        return right - left
