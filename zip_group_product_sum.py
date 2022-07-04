"""
в массиве первое число отвечает за значение, второе за количетво
по сути надо развернуть массивы, попарно перемножить и сложить
assert zip_sum([[1, 2]], [[2,1], [3, 1]]) == 5 # 1 * 2 + 1 * 3
"""


def dotproduct(a: list[list[int]], b: list[list[int]]) -> int:
    """идем с конца, уже отработанные группы удаляем"""
    res = 0
    while a and b:
        min_diff = min(a[-1][1], b[-1][1])
        res += a[-1][0] * b[-1][0] * min_diff
        a[-1] = (a[-1][0], a[-1][1] - min_diff)
        b[-1] = (b[-1][0], b[-1][1] - min_diff)
        if a[-1][1] == 0:
            a.pop()
        if b[-1][1] == 0:
            b.pop()
    if a or b:
        print("Invalid argument")
        return
    return res


def zip_sum(l1: list[list[int]], l2: list[list[int]]) -> int:
    """итеририруемся с начала и двигаем указатель вперёд, если обработали все элементы из этой группы"""
    p1 = 0
    p2 = 0
    result = 0
    while p1 < len(l1) and p2 < len(l2):
        count = min(l1[p1][1], l2[p2][1])
        result += count * (l1[p1][0] * l2[p2][0])
        l1[p1][1] -= count
        l2[p2][1] -= count
        if l1[p1][1] == 0:
            p1 += 1
        if l2[p2][1] == 0:
            p2 += 1
    if p1 < len(l1) or p2 < len(l2):
        print("Invalid argument")
        return
    return result


assert zip_sum([[1, 2]], [[2,1], [3, 1]]) == 5
assert zip_sum([[1, 3]], [[2,1], [3, 1]]) == None # разные длины, слишком много единиц в первом массиве
assert zip_sum([[2, 2], [3, 1]], [[2,1], [3, 1], [4, 1]]) == 22
