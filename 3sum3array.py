from collections import Counter


def three_sum_in_three_array(target: int, arr_1: list[int], arr_2: list[int], arr_3: list[int]) -> int:
    counter_1 = Counter(arr_1)
    result = 0
    for num_2 in arr_2:
        for num_3 in arr_3:
            if (target - num_2 - num_3) in counter_1:
                result += counter_1[target - num_2 - num_3]
                print(target - num_2 - num_3, num_2, num_3, "-", counter_1[target - num_2 - num_3])
    return result


def group_by(nums: list[int]) -> list[list[int, int]]:
    if not nums:
        return []
    result = [[nums[0], 1]]
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            result[-1][1] += 1
        else:
            result.append([nums[i], 1])
    return result

def two_sum_in_two_array(target: int, arr_1: list[int], arr_2: list[int]) -> int:
    result = 0
    arr_1 = sorted(group_by(arr_1))
    arr_2 = sorted(group_by(arr_2))
    # print(arr_1)
    # print(arr_2)
    i = 0
    j = len(arr_2) - 1
    while i < len(arr_1) and j >= 0:
        # print(f'{arr_1[i][0]=} {i=}')
        # print(f'{arr_2[j][0]=} {j=}')
        curr_sum = arr_1[i][0] + arr_2[j][0]
        if curr_sum == target:
            result += arr_1[i][1] * arr_2[j][1]
            print(arr_1[i], arr_2[j])
            i += 1
        elif curr_sum > target:
            j -= 1
        else:
            i += 1
    
    return result


print(
    two_sum_in_two_array(
        8, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]
    )
)


# def three_sum_in_three_array(target: int, arr_1: list[int], arr_2: list[int], arr_3: list[int]) -> int:
#     arr_1 = sorted(group_by(arr_1))
#     arr_2 = sorted(group_by(arr_2))
#     arr_3 = sorted(group_by(arr_3))
#     result = 0
#     for num_1, cnt_1 in arr_1:

        

# print(
#     three_sum_in_three_array(
#         # 3, 
#         # [1, 1, 1],
#         # [1, 1, 1],
#         # [1, 1, 1],
#         4, 
#         [2, 1, 1],
#         [2, 1, 1],
#         [1, 2, 1],
#     )
# )
