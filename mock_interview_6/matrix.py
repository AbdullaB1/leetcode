def solution(matrix):
    n = len(matrix)
    # главная это matrix[i][i]
    # побочная это matrix[i][n - i + 1]
    result = 0
    for i in range(n):
        result += matrix[i][i]
    for i in range(n):
        result += matrix[i][n - i + 1]
    if n % 2 == 1:
        result -= matrix[n//2][n//2]
    return result


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [9, 10, 11, 12]
          ]

print(
    solution(
        matrix
    )
)
