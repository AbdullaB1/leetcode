from typing import List

# Не проходит по времени, падает на 50 тесте из 80
# Проблема скорее всего в хранении уже пройденных вершин в set, и передаче его дальше
# class Solution:
#     def check_next_letter(self, board: List[List[str]], letter: str, row, col, visited: set) -> list[tuple]:
#         m = len(board)
#         n = len(board[0])
#         row_diffs = [1, -1, 0, 0]
#         col_diffs = [0, 0, 1, -1]
#         result = []
#         for drow, dcol in zip(row_diffs, col_diffs):
#             cur_row = row + drow
#             cur_col = col + dcol
#             if 0 <= cur_row < m and 0 <= cur_col < n:
#                 if board[cur_row][cur_col] == letter:
#                     if (cur_row, cur_col) not in visited:
#                         result.append((cur_row, cur_col))
#         return result

#     def exist(self, board: List[List[str]], word: str) -> bool:
#         m = len(board)
#         n = len(board[0])
#         starts = []
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == word[0]:
#                     starts.append((i, j))
#         if not starts:
#             return False

#         if len(word) == 1:
#             return True

#         for start in starts:
#             stack = [[start, {start}, 1]]
#             while stack:
#                 curr, visited, index = stack.pop()
#                 nexts = self.check_next_letter(
#                     board, word[index], curr[0], curr[1], visited)
#                 if nexts and index >= len(word) - 1:
#                     return True
#                 for n in nexts:
#                     new_visited = {item for item in visited}
#                     new_visited.add(n)
#                     stack.append([n, new_visited, index + 1])

#         return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] += "_"
                    if self.traverse(board, word[1:], i, j):
                        return True
                    board[i][j] = board[i][j][0]
        return False

    def traverse(self, board: List[List[str]], word: str, row: int, col: int) -> bool:
        if len(word) == 0:
            return True

        m = len(board)
        n = len(board[0])
        row_diffs = [1, -1, 0, 0]
        col_diffs = [0, 0, 1, -1]

        for drow, dcol in zip(row_diffs, col_diffs):
            cur_row = row + drow
            cur_col = col + dcol
            if 0 <= cur_row < m and 0 <= cur_col < n:
                if board[cur_row][cur_col] == word[0]:
                    board[cur_row][cur_col] += "_"
                    if self.traverse(board, word[1:], cur_row, cur_col):
                        return True
                    board[cur_row][cur_col] = board[cur_row][cur_col][0]

        return False


s = Solution()
print(
    s.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCCED"
    )
)
