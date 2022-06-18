from itertools import cycle
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        row = col = top = left = 0
        right = bottom = n - 1
        cur_dir = next(directions)
        matrix[0][0] = 1
        value = 2
        while top <= bottom and left <= right:
            if top <= row + cur_dir[0] <= bottom and left <= col + cur_dir[1] <= right:
                row += cur_dir[0]
                col += cur_dir[1]
                matrix[row][col] = value
                value += 1
            else:
                if cur_dir[0] == 1:
                    right -= 1
                elif cur_dir[0] == -1:
                    left += 1
                elif cur_dir[1] == 1:
                    top += 1
                elif cur_dir[1] == -1:
                    bottom -= 1
                cur_dir = next(directions)
        return matrix
