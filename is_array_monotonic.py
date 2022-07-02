def is_monotonic_1(nums: list[int]) -> bool:
    if len(nums) <= 2:
        return True

    if nums[0] == nums[-1]:
        curr = nums[0]
        for num in nums:
            if num != curr:
                return False
        return True

    if nums[0] < nums[-1]:
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < prev:
                return False
            prev = nums[i]
        return True

    if nums[0] > nums[-1]:
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > prev:
                return False
            prev = nums[i]
        return True


# более элегантное решение
def is_monotonic(nums: list[int]) -> bool:
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False

    print(nums, f"{increasing=} {decreasing=}")

    return increasing or decreasing


assert is_monotonic([]) == True
assert is_monotonic([-1]) == True
assert is_monotonic([-1, 2]) == True
assert is_monotonic([1, -22]) == True
assert is_monotonic([1, 2, 2, 3]) == True
assert is_monotonic([6, 5, 4, 4]) == True
assert is_monotonic([1, 3, 2]) == False
assert is_monotonic([-2, -1, 2, 3]) == True
assert is_monotonic([-2, -1, -2, 3]) == False
assert is_monotonic([3, 2, 2, -3]) == True
assert is_monotonic([3, 2, 2, -3, 5]) == False
