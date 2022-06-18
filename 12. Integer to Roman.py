class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        result = []
        i = 0
        while num > 0:
            while romans[i][0] > num:
                i += 1
            num -= romans[i][0]
            result.append(romans[i][1])

        return ''.join(result)
