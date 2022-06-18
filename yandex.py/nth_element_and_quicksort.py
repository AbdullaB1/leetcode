def partition(nums: list[int], l: int, r: int) -> int:
    if l == r:
        return l
    elif l > r:
        return
    delimeter = nums[r - 1]
    first = l
    for i in range(l, r):
        if nums[i] < delimeter:
            nums[first], nums[i] = nums[i], nums[first]
            first += 1
    nums[first], nums[r - 1] = nums[r - 1], nums[first]
    return first


def hoar_partition(nums: list[int], l: int, r: int) -> int:
    if l == r:
        return l
    elif l > r:
        return
    delimeter = nums[l + r // 2]

    while True:
        while nums[l] <= delimeter:
            l += 1
        while nums[r] > delimeter:
            r -= 1
        if l >= r:
            return r
        nums[l], nums[r] = nums[r], nums[l]


def hoar_quicksort(nums: list[int], l: int, r: int):
    if l >= r:
        return
    print(l, r)
    # работате и без этого, но только для разделения по ламуто, надо разобраться почему
    if r - l < 2:
        if nums[l] > nums[r - 1]:
            nums[l], nums[r - 1] = nums[r - 1], nums[l]
        return
    mid = hoar_partition(nums, l, r)
    hoar_quicksort(nums, l, mid)
    hoar_quicksort(nums, mid + 1, r)


nums = [5, 4, 3, 7, 10, 11, 2]
hoar_quicksort(
    nums,
    0,
    len(nums) - 1
)
print(nums)


def nth_element(nums: list[int], k: int) -> int:
    if k > len(nums) - 1 or k < 0:
        return -1
    l = 0
    r = len(nums)
    print(l, r)
    while True:
        mid = partition(nums, l, r)
        if mid == k:
            return nums[mid]
        elif k < mid:
            r = mid
        else:
            l = mid + 1
        print(l, r)


def quicksort(nums: list[int], l: int, r: int):
    if l >= r:
        return
    print(l, r)
    # работате и без этого
    # if r - l < 2:
    #     if nums[l] > nums[r - 1]:
    #         nums[l], nums[r - 1] = nums[r - 1], nums[l]
    #     return
    mid = partition(nums, l, r)
    quicksort(nums, l, mid)
    quicksort(nums, mid + 1, r)


# print(
#     nth_element(
#         [22, 33, 11, 5],
#         3
#     )
# )

# nums = [33]
# print(
#     partiotion(
#         nums,
#         0,
#         len(nums)
#     ),
#     nums
# )


# nums = [1]

# quicksort(
#     nums,
#     0,
#     len(nums)
# )
# print(nums)
