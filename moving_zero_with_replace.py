def moving_zero(nums: list[int]) -> int:
    """решение с prev не работает, потому что мы заменяем лишние числа на _"""
    first = 0
    # начианем с первого элемента
    for i in range(1, len(nums)):
        if nums[i] != nums[first]:
            # first плюсуем заранее
            first += 1
            nums[first], nums[i] = nums[i], nums[first]
        else:
            nums[i] = '_'
    return first

a = [1, 1, 2, 3, 3, 4]
print(
    moving_zero(
        a
    )
)
print(a)