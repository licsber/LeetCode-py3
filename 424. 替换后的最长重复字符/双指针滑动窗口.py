from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        nums = defaultdict(int)
        maxn = left = right = 0

        n = len(s)
        while right < n:
            nums[s[right]] += 1
            maxn = max(maxn, nums[s[right]])
            if maxn + k < right - left + 1:
                nums[s[left]] -= 1
                left += 1
            right += 1
        return right - left
