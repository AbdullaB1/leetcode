def intersections(arr_1: list[int], arr_2: list[int]) -> list[int]:
    set1 = set()
    set2 = set()
    result = []
    for elem_1, elem_2 in zip(arr_1, arr_2):
        curr = result[-1] if result else 0
        if elem_1 == elem_2 and (elem_1 not in set1 or elem_2 not in set2):
            curr += 1
        else:
            if elem_1 not in set1 and elem_1 in set2:
                curr += 1
            if elem_2 not in set2 and elem_2 in set1:
                curr += 1
        set1.add(elem_1)
        set2.add(elem_2)
        result.append(curr)
    return result


assert intersections([2, 1, 3], [1, 2, 4]) == [0, 2, 2]
assert intersections([1, 3, 2, 2], [2, 1, 3, 2]) == [0, 1, 3, 3]
assert intersections([], []) == []
assert intersections([2], [1]) == [0]
assert intersections([2], [2]) == [1]
assert intersections([2, 1, 3, 4], [1, 2, 4, 3]) == [0, 2, 2, 4]
