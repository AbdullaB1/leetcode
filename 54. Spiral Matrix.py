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


s = Solution()
print(
    s.spiralOrder(
        # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ]
        # [[1, 2, 3]]
        # [[1], [2], [3]]
    )
)
