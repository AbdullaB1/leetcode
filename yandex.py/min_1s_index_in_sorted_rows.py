def min_1s_index_in_sorted_rows(matrix: list[list[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    min_index = m - 1
    for i in range(n):
        while min_index >= 0 and matrix[i][min_index] == 1:
            min_index -= 1
    return min_index + 1


print(
    min_1s_index_in_sorted_rows(
        [
            [0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 1, 1, 1],
        ]
    )
)
print(
    min_1s_index_in_sorted_rows(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
        ]
    )
)
