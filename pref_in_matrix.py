class PrefMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        self.pref: list[list[int]] = matrix
        self.calculate_pref_2()

    def calculate_pref(self) -> None:
        rows = len(self.pref)
        cols = len(self.pref[0])
        for i in range(0, rows):
            for j in range(1, cols):
                self.pref[i][j] += self.pref[i][j - 1]
        print(*self.pref, sep='\n')
        for i in range(1, rows):
            for j in range(0, cols):
                self.pref[i][j] += self.pref[i - 1][j]
        print(*self.pref, sep='\n')

    # рассчет префиксной суммы за один проход по матрице
    def calculate_pref_2(self) -> None:
        rows = len(self.pref)
        cols = len(self.pref[0])
        for i in range(rows):
            row_sum = 0
            for j in range(cols):
                row_sum += self.pref[i][j]
                self.pref[i][j] = row_sum
                self.pref[i][j] += self.pref[i - 1][j] if i - 1 >= 0 else 0
        

    def query(self, x1: int, y1: int, x2: int, y2: int) -> int:
        upper = (self.pref[x1 - 1][y2] if x1 - 1 >= 0 else 0)
        left = (self.pref[x2][y1 - 1] if y1 - 1 >= 0 else 0)
        upper_left_corner = (
            self.pref[x1 - 1][y1 - 1] if (0 <= x1 - 1 and 0 <= y1 - 1) else 0)
        print(self.pref[x2][y2], upper, left, upper_left_corner)
        return self.pref[x2][y2] - upper - left + upper_left_corner


prefmatrix = PrefMatrix(
    # [
    #     [1, -1, 3],
    #     [4, 9, 10],
    #     [1, 2, 3]
    # ]
    [[1, 2, 3]]
)

# print(prefmatrix.query(1, 1, 2, 2))
print(prefmatrix.query(0, 1, 0, 2))
