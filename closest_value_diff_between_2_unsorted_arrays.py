import math


"""
Наименьшая по модулю разница значений между двумя несортированными массивами
[1,2,11,5],[4,12,19,23,127] -> 1
"""


def find_closest(arr_1: list[int], arr_2: list[int]) -> int:
    arr_1.sort()
    arr_2.sort()
    p1 = 0
    p2 = 0
    result = math.inf
    while p1 < len(arr_1) and p2 < len(arr_2):
        result = min(result, abs(arr_1[p1] - arr_2[p2]))
        if arr_1[p1] < arr_2[p2]:
            p1 += 1
        else:
            p2 += 1
    if math.isinf(result):
        return -1
    return result


assert find_closest([], [4, 12, 19, 23, 127]) == -1
assert find_closest([4, 12, 19, 23, 127], []) == -1
assert find_closest([1, 2, 11, 5], [4, 12, 19, 23, 127]) == 1
assert find_closest([100, 10, 20, 50], [200, 300, 400, 15, 500]) == 5
