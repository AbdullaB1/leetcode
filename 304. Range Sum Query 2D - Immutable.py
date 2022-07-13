class NumMatrix:
    """
    premium (решить потом) - https://leetcode.com/problems/range-sum-query-2d-mutable/
    """
    def __init__(self, matrix: list[list[int]]):
        self.pref: list[list[int]] = matrix
        self.calculate_pref()

    def calculate_pref(self) -> None:
        rows = len(self.pref)
        cols = len(self.pref[0])
        for i in range(rows):
            row_sum = 0
            for j in range(cols):
                row_sum += self.pref[i][j]
                self.pref[i][j] = row_sum
                self.pref[i][j] += self.pref[i - 1][j] if i - 1 >= 0 else 0

    def sumRegion(self, x1: int, y1: int, x2: int, y2: int) -> int:
        upper = (self.pref[x1 - 1][y2] if x1 - 1 >= 0 else 0)
        left = (self.pref[x2][y1 - 1] if y1 - 1 >= 0 else 0)
        upper_left_corner = (
            self.pref[x1 - 1][y1 - 1] if (0 <= x1 - 1 and 0 <= y1 - 1) else 0)
        # print(self.pref[x2][y2], upper, left, upper_left_corner)
        return self.pref[x2][y2] - upper - left + upper_left_corner
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
