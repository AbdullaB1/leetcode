def flatten(arr: list) -> list[int]:
    # нужно поместить именно нераспакованный список, иначе порядок не сохранится
    stack = [arr]
    result = []
    while stack:
        elem = stack.pop()
        if not isinstance(elem, list):
            result.append(elem)
        else:
            stack.extend([elem[i] for i in range(len(elem) - 1, -1, -1)])
    return result


print(flatten([1, 2, 3, [4, 5, [6, 7], 8], 9]))
assert flatten([1, 2, 3, [4, 5, [6, 7], 8], 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert flatten([1, [2, 3], [4, 5, [6, 7], [8]], 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
