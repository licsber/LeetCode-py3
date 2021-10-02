class Solution:
    digits = '0123456789abcdef'

    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        elif num < 0:
            num = 2 ** 32 + num

        ans = ''
        while num:
            digit = num % 16
            ans += self.digits[digit]
            num //= 16

        return ans[::-1]
