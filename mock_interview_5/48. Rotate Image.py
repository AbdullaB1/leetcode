from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j -
                                        1] = matrix[i][n - j - 1], matrix[i][j]

    def rotate_1(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        while left < right and top < bottom:
            for i in range(bottom - top):
                a = matrix[top][left + i]
                b = matrix[top + i][right]
                c = matrix[bottom][right - i]
                d = matrix[bottom - i][left]
                # print(a, b, c, d)
                matrix[top][left + i] = d
                matrix[top + i][right] = a
                matrix[bottom][right - i] = b
                matrix[bottom - i][left] = c
                # print(
                #     matrix[top][left + i],
                #     matrix[top + i][right],
                #     matrix[bottom][right - i],
                #     matrix[bottom - i][left]
                # )

            top += 1
            bottom -= 1
            left += 1
            right -= 1
