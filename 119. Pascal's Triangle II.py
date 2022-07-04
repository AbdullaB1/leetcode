class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for _ in range(rowIndex):
            new_row = [0] * (len(row) + 1)
            for i in range(len(new_row)):
                sum_1 = row[i - 1] if (i - 1) >= 0 else 0
                sum_2 = row[i] if i < len(row) else 0
                new_row[i] = sum_1 + sum_2
            row = new_row
        return row
