from typing import List


class Solution:
    # Time: O(m*n)
    # Space: O(n) не обязательно хранить всю доп матрицу
    # можно просто оперировать прошлой и текущей строкой
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prev = [0 for i in range(cols + 1)]
        max_area = 0
        for i in range(1, rows + 1):
            dp = [0 for i in range(cols + 1)]
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(
                        min(prev[j], dp[j - 1]),
                        prev[j - 1]
                    ) + 1
                    max_area = max(max_area, dp[j])
                else:
                    dp[j] == 0
            prev = dp
        return max_area ** 2

    # Time: O(m*n)
    # Space: O(m*n)
    def maximalSquare_1(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for i in range(cols + 1)] for i in range(rows + 1)]
        max_area = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(
                        min(dp[i][j - 1], dp[i - 1][j]),
                        dp[i - 1][j - 1]
                    ) + 1
                    max_area = max(max_area, dp[i][j])
        return max_area ** 2


s = Solution()
s.maximalSquare(
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
)
