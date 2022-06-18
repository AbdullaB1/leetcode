from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col = row = left = right = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        result = []
        prev_step = 1
        while top <= bottom and left <= right:
            print(row, col)
            result.append(matrix[row][col])
            if prev_step == 1:
                if col < right:
                    col += 1
                else:
                    top += 1
                    row += 1
                    prev_step = 2
            elif prev_step == 2:
                if row < bottom:
                    row += 1
                else:
                    right -= 1
                    col -= 1
                    prev_step = 3
            elif prev_step == 3:
                if col > left:
                    col -= 1
                else:
                    bottom -= 1
                    row -= 1
                    prev_step = 4
            elif prev_step == 4:
                if row > top:
                    row -= 1
                else:
                    left += 1
                    col += 1
                    prev_step = 1
        return result

        # m = len(matrix)
        # n = len(matrix[0])
        # result = 0
        # col = 0
        # row = 0
        # left = 0
        # right = n - 1
        # top = 0
        # bottom = m - 1
        # result = []
        # prev_step = 1
        # while True:
        #     print(row, col)
        #     result.append(matrix[row][col])
        #     if prev_step == 1:
        #         if col < right:
        #             col += 1
        #         elif row < bottom:
        #             top += 1
        #             row += 1
        #             prev_step = 2
        #         else:
        #             break
        #     elif prev_step == 2:
        #         if row < bottom:
        #             row += 1
        #         elif col > left:
        #             right -= 1
        #             col -= 1
        #             prev_step = 3
        #         else:
        #             break
        #     elif prev_step == 3:
        #         if col > left:
        #             col -= 1
        #         elif row > top:
        #             bottom -= 1
        #             row -= 1
        #             prev_step = 4
        #         else:
        #             break
        #     elif prev_step == 4:
        #         if row > top:
        #             row -= 1
        #         elif col < right:
        #             left += 1
        #             col += 1
        #             prev_step = 1
        #         else:
        #             break
        # return result


def SpiralMatrix(matrix: list[list[int]]) -> list[int]:
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bot = len(matrix) - 1
    result = []
    while True:
        for i in range(left, right):
            result.append(matrix[top][i])
        for i in range(top, bot):
            result.append(matrix[i][right])
        for i in range(right, left, -1):
            result.append(matrix[bot][i])
        for i in range(bot, top, -1):
            result.append(matrix[i][left])
        left = left + 1
        right = right - 1
        top = top + 1
        bot = bot - 1
        if top < bot and right < left:
            return result
        if left == right == top == bot:
            result.append(matrix[top][top])
            return result
        if top == bot and right != left:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            return result
        if right == left and top != bot:
            for i in range(top, bot + 1):
                result.append(matrix[i][right])
            return result


print(
    SpiralMatrix(
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
        # [
        #     [1, 2, 3],
        #     [4, 5, 6],
        #     [7, 8, 9],
        #     [10, 11, 12]
        # ]
        # [[1, 2, 3]]
        # [[1], [2], [3]]
    )
)
