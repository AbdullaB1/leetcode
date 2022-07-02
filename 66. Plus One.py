class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        remaining = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += remaining
            if digits[i] > 9:
                digits[i] = 0
                remaining = 1
            else:
                return digits
        digits.append(0)
        digits[0] = 1
        return digits
