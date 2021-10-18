class Solution:
    def findComplement(self, num: int) -> int:
        first_one = 0
        while num >= (1 << (first_one + 1)):
            first_one += 1

        mask = (1 << (first_one + 1)) - 1
        return num ^ mask
