# >> [0, 10, 0, 1, 2, 3, 0, 0, 4, 0]
# << [10, 1, 2, 3, 4, 0, 0, 0, 0, 0]


# [0, 10, 0, 1, 2, 3, 0, 0, 4, 0]

# [0]
# [0, 10] -> [10, 0]
# [10, 0, 0]
# [10, 0, 0, 1] -> [10, 1, 0, 0]

# [10, 1, 2, 0, 0]

def sort_zeros_to_back(nums: list[int]) -> list[int]:
    first = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[first], nums[i] = nums[i], nums[first]
            first += 1
    return nums


# https://ru.wikipedia.org/wiki/Быстрая_сортировка#Разбиение_Ломуто
