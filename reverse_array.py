import copy


def reverse_1(nums: list[int]) -> None:
    if not nums:
        return
    p1 = 0
    p2 = len(nums) - 1
    while p1 < p2:
        nums[p1], nums[p2] = nums[p2], nums[p1]
        p1 += 1
        p2 -= 1


# более короткое и красивое решение
def reverse(nums: list[int]) -> None:
    for i in range(len(nums) // 2):
        nums[i], nums[-i - 1] = nums[-i - 1], nums[i]


arrays = [
    [],
    [1],
    [2, 1],
    [5, 4, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
]
arrays_2 = copy.deepcopy(arrays)
for a in arrays:
    reverse(a)
    a.reverse()
for a1, a2 in zip(arrays, arrays_2):
    assert a1 == a2
