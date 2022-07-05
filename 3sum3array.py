from collections import Counter


def three_sum_in_three_array(target: int, arr_1: list[int], arr_2: list[int], arr_3: list[int]) -> int:
    """
    решение бес сортировки и с доп памятью
    можно оптимизировать 2 вложенных цикла на манер следующего решения с сортировкой, 
    сейчас там полный перебор 
    """
    counter_1 = Counter(arr_1)
    result = 0
    for num_2 in arr_2:
        for num_3 in arr_3:
            if (target - num_2 - num_3) in counter_1:
                result += counter_1[target - num_2 - num_3]
                # print(target - num_2 - num_3, num_2, num_3, "-", counter_1[target - num_2 - num_3])
    return result 


def three_sum_in_three_array(target: int, arr_1: list[int], arr_2: list[int], arr_3: list[int]) -> int:
    """
    три массива, найти количество таких троек i, j, k где arr_1[i] + arr_2[j] + arr_3[k] == target
    1 <= len(arr_1) <= len(arr_2) <= len(arr_3)
    """
    arr_1.sort()
    arr_2.sort()
    arr_3.sort()
    result = 0
    for i, num_1 in enumerate(arr_1):
        l =  0
        r = len(arr_3) -1
        sub_target = target - num_1
        while l < len(arr_2) and  r >= 0:
            if arr_2[l] + arr_3[r] < sub_target:
                l += 1
                continue
            if arr_2[l] + arr_3[r] > sub_target:
                r -= 1
                continue
            l_count = 1
            l += 1
            while l < len(arr_2) and arr_2[l] == arr_2[l - 1]:
                l_count += 1
                l += 1
            r_count = 1
            r -= 1
            while r >= 0 and arr_3[r] == arr_3[r + 1]:
                r_count += 1
                r -= 1 
            result += l_count * r_count
            # print(f"{result=} {i=} {l=} {l_count=} {r=} {r_count=}")
    return result


print(
    three_sum_in_three_array(
        4, 
        [2, 1, 1],
        [2, 1, 1],
        [1, 2, 1],
    )
)

assert three_sum_in_three_array(3, [1, 1, 1], [1, 1, 1], [1, 1, 1]) == 27
assert three_sum_in_three_array(4, [1, 1, 1], [1, 1, 1], [1, 1, 1]) == 0
assert three_sum_in_three_array(2, [1, 1, 1], [1, 1, 1], [1, 1, 1]) == 0
assert three_sum_in_three_array(4, [2, 1, 1], [2, 1, 1], [2, 1, 1]) == 12
