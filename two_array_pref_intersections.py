"""длина массивов всегда совпадает"""
def intersections(arr1: list[int], arr2: list[int]) -> list[int]:
    set1 = set()
    set2 = set()
    result = []
    for elem1, elem2 in zip(arr1, arr2):
        curr = result[-1] if result else 0
        if elem1 == elem2 and (elem1 not in set1 or elem2 not in set2):
            curr += 1
        else:
            if elem1 != elem2 and elem1 not in set1 and elem1 in set2:
                curr += 1
            if elem1 != elem2 and elem2 not in set2 and elem2 in set1:
                curr += 1
        set1.add(elem1)
        set2.add(elem2)
        result.append(curr)
    return result


print(intersections([1,3,2,2], [2,1,3,2]))
assert intersections([1, 1], [2, 1]) == [0, 1]
assert intersections([1,3,2,2], [2,1,3,2]) == [0, 1, 3, 3]
assert intersections([1,2,3,4], [4,3,2,1]) == [0, 0, 2, 4]
