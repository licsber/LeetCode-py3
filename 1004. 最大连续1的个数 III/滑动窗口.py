from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        zero = 0
        ans = -1
        length = len(nums)
        while right != length:
            if nums[right] == 0:
                zero += 1

            right += 1
            while zero > k and left < right:
                if nums[left] == 0:
                    zero -= 1

                left += 1

            ans = max(ans, right - left)

        return ans
