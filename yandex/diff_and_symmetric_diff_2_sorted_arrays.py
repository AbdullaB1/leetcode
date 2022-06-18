# нерабочее решение с собеса Вовы
def print_array(nums1, nums2):
    i = j = 0
    result = []
    while i < len(nums1) or j <= len(nums2):
        if j == len(nums2) or nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        elif nums1[i] == nums2[j]:
            i += 1
        else:
            j += 1
    return result


# все числа, которые ест в первом массиве, но которых нет во втором
def Diff(nums1: list[int], nums2: list[int]) -> list[int]:
    i = j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            # result.append(nums2[j])
            j += 1
        else:
            i += 1
            j += 1

    while i < len(nums1):
        result.append(nums1[i])
        i += 1

    # while j < len(nums2):
    #     result.append(nums2[j])
    #     j += 1

    return result

# симмертичная разница 2 отсортированных массивов


def symmDiff(nums1: list[int], nums2: list[int]) -> list[int]:
    i = j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            result.append(nums2[j])
            j += 1
        else:
            i += 1
            j += 1

    while i < len(nums1):
        result.append(nums1[i])
        i += 1

    while j < len(nums2):
        result.append(nums2[j])
        j += 1

    return result


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    i = j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            # result.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            # result.append(nums2[j])
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1

    return result


def like_sql_join(nums1: list[int], nums2: list[int]) -> list[int]:
    i = j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            # result.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            # result.append(nums2[j])
            j += 1
        else:
            result.append(nums1[i])
            j += 1

    return result


a = [1, 1, 1, 2, 4, 6, 7, 8, 9]
b = [1, 1, 1, 3, 4, 5]

print(
    Diff(
        a, b
    )
)

print(
    symmDiff(
        a, b
    )
)

print(
    intersect(
        a, b
    )
)

print(
    like_sql_join(
        [3, 4], [1, 2, 3, 3, 4, 4, 4, 5, 6, 7]
    )
)
