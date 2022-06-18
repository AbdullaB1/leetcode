def findDisappearedNumbers(nums: list[int]) -> list[int]:
    i = 0
    cnt = 0
    while i != len(nums):
        cnt += 1
        pos = nums[i] - 1
        if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
        else:
            i += 1

    result = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            result.append(i + 1)
    print(cnt)
    return result


findDisappearedNumbers(
    list(map(int, input().split()))
)
