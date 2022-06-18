from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        row_contain_zero = False
        col_contain_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                col_contain_zero = True
                break

        for i in range(n):
            if matrix[0][i] == 0:
                row_contain_zero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_contain_zero:
            for i in range(n):
                matrix[0][i] = 0

        if col_contain_zero:
            for i in range(m):
                matrix[i][0] = 0

        # с использлованием доп памяти
        # lines = set()
        # cols = set()
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             lines.add(i)
        #             cols.add(j)
        # for i in range(m):
        #     for j in range(n):
        #         if i in lines or j in cols:
        #             matrix[i][j] = 0
