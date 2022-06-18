class PrefMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix
        self.pref = matrix
        self.calculate_pref()

    def calculate_pref(self) -> None:
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        for i in range(0, rows):
            for j in range(1, cols):
                self.pref[i][j] += self.pref[i][j - 1]
        print(*self.pref, sep='\n')
        for i in range(1, rows):
            for j in range(0, cols):
                self.pref[i][j] += self.pref[i - 1][j]
        print(*self.pref, sep='\n')

    def query(self, x1: int, y1: int, x2: int, y2: int) -> int:
        upper = (self.pref[x1 - 1][y2] if x1 - 1 >= 0 else 0)
        left = (self.pref[x2][y1 - 1] if y1 - 1 >= 0 else 0)
        upper_left_corner = (
            self.pref[x1 - 1][y1 - 1] if 0 <= x1 and 0 <= y1 else 0)
        print(self.pref[x2][y2], upper, left, upper_left_corner)
        return self.pref[x2][y2] - upper - left + upper_left_corner


prefmatrix = PrefMatrix(
    [
        [1, -1, 3],
        [4, 9, 10],
        [1, 2, 3]
    ]
)

print(prefmatrix.query(1, 1, 2, 2))


class PrefMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        # создание матрицы
        self.mas = []
        for i in range(len(matrix)):
            self.mas.append([0] * len(matrix[0]))

        # пройдем по всем точкам этой матрицы
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # сложим все строчки
                sub = 0
                for k in range(i + 1):
                    sub += sum(matrix[k][0:j + 1])
                self.mas[i][j] = sub
        print(*self.mas)


prefmatrix = PrefMatrix(
    [
        [1, -1, 3],
        [4, 9, 10],
        [1, 2, 3]
    ]
)
