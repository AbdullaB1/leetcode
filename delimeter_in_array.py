def find_delimeter(arr: list[int]) -> int:
    left_pref = sum(arr)
    right_pref = 0
    for i in range(len(arr) - 1, -1, -1):
        left_pref -= arr[i]
        right_pref += arr[i + 1] if (i + 1) < len(arr) else 0
        if left_pref == right_pref:
            return i
    return -1


assert find_delimeter([-7,1,5,2,-4,3,0]) == 6
assert find_delimeter([1, 1, 1]) == 1
assert find_delimeter([1, -100, 1]) == 1
assert find_delimeter([1, -100]) == -1
assert find_delimeter([-100]) == 0
assert find_delimeter([10, -100, 1, 2, 3, 4]) == 1
