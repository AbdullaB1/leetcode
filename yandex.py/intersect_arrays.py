from collections import defaultdict


def list_to_dict(arr: list[int]) -> dict:
    result = defaultdict(int)
    for el in arr:
        result[el] += 1
    return result


def intersect(one: list[int], two: list[int]) -> list[int]:
    map_1 = list_to_dict(one)
    result = []

    for el in two:
        count = map_1[el]
        if count > 0:
            result.append(el)
            map_1[el] -= 1
    return result


def defferance(one: list[int], two: list[int]) -> list[int]:
    map_1 = list_to_dict(one)

    for el in two:
        if el in map_1:
            map_1[el] -= 1
            if map_1[el] == 0:
                map_1.pop(el)

    result = []
    for key, value in map_1.items():
        result.extend([key for _ in range(value)])

    return result


def symmetric_defferance(one: list[int], two: list[int]) -> list[int]:
    map_1 = list_to_dict(one)

    for el in two:
        if el in map_1:
            map_1[el] -= 1

    result = []
    for key, value in map_1.items():
        result.extend([key for _ in range(abs(value))])

    return result


# если нужно просто объединить, то можно через extend или +
# если же нужно для каждого числа брать максимум, тогда можно так
def union(one: list[int], two: list[int]) -> list[int]:
    map_1 = defaultdict(lambda: [0, 0])
    for num in one:
        map_1[num][0] += 1
    for num in two:
        map_1[num][1] += 1
    result = []
    for key in map_1:
        max_count = max(map_1[key][0], map_1[key][1])
        result.extend([key for _ in range(max_count)])
    return result


print(union(
    [1, 1, 2, 2, 3, 4],
    [1, 2, 2, 2, 3, 3]
))
