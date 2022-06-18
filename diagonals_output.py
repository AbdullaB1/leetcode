# чуть более усложненная вресия на литкоде
# https://leetcode.com/problems/diagonal-traverse/


def findDiagonalOrder(matrix: list[list[int]]):
    n = len(matrix)
    count = 1
    for start in range(n):  # идет вниз
        i = start
        for j in range(count):
            print(matrix[i][j], end=' ')
            i -= 1
        print()
        count += 1
    count -= 0 if n % 2 else 1  # т.к. лишний раз добавили на выходе
    for start in range(1, n):
        j = start
        for i in range(n - 1, n - count, -1):
            print(matrix[i][j], end=' ')
            j += 1
        print()
        count -= 1


print(findDiagonalOrder(
    [
        [1, 2, 3, 4],
        [4, 5, 6, 5],
        [7, 8, 9, 6],
        [7, 8, 9, 6]
    ]
))
print(findDiagonalOrder(
    [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6]
    ]
))
