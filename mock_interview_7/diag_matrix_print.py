def print_diags(matrix):
    count = 1
    for start in range(len(matrix)):
        i = start
        for j in range(count):
            print(matrix[i][j], end=' ')
            i -= 1
        print()
        count += 1
    count = len(matrix) - 1
    for start in range(1, len(matrix[0])):
        j = start
        for i in range(len(matrix) - 1, count, -1):
            print(matrix[i][j], end=' ')
            i -= 1
        print()
        count -= 1


def findDiagonalOrder(matrix):
    d = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i + j not in d:
                d[i+j] = [matrix[i][j]]
            else:
                d[i+j].append(matrix[i][j])
    ans = []
    for entry in d.items():
        if entry[0] % 2 == 0:
            [ans.append(x) for x in entry[1]]
        else:
            [ans.append(x) for x in entry[1]]
    return ans


print(findDiagonalOrder(
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]
))
