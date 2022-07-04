class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            new_row = []
            for i in range(len(res[-1]) + 1):
                sum_1 = res[-1][i - 1] if i - 1 >= 0 else 0
                sum_2 = res[-1][i] if i < len(res[-1]) else 0
                new_row.append(sum_1 + sum_2)
            res.append(new_row)
        return res
