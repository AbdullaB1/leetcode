from typing import List


class Solution:
    # более оптимальное решение, мы не меняем исходную матрицу
    # и преобразуем каждый раз строку для передачи в функцию на основе предидущей
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        dp = [0] * rows
        for col in range(cols):
            for i in range(rows):
                dp[i] = dp[i] + 1 if matrix[i][col] == "1" else 0
            print(dp)
            max_area = max(
                max_area,
                self.largestRectangleArea(dp)
            )
        return max_area

    # 84. Largest Rectangle in Histogram
    # https://leetcode.com/problems/largest-rectangle-in-histogram/
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                cur_h = heights[stack.pop()]
                cur_w = i - stack[-1] - 1
                max_area = max(max_area, cur_h * cur_w)
            stack.append(i)

        while stack[-1] != -1:
            cur_h = heights[stack.pop()]
            cur_w = len(heights) - stack[-1] - 1
            max_area = max(max_area, cur_h * cur_w)
        return max_area

    # первоначальное решение, в котором преобразуется вся матрица

    def maximalRectangle_1(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            curr = 0
            for j in range(cols):
                curr += int(matrix[i][j])
                curr *= int(matrix[i][j])
                matrix[i][j] = curr
        # print(*matrix, end="\n")
        max_area = 0
        for col in range(cols):
            max_area = max(
                max_area,
                # не очень оптимально по памяти,
                # написал так, чтобы легко переиспользовать решение из задачи
                # 84. Largest Rectangle in Histogram
                self.largestRectangleArea(
                    [matrix[i][col] for i in range(rows)])
            )
        return max_area
