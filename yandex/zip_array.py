
def get_interval(start, end):
    if start == end:
        return str(start)
    else:
        return f"{start}->{end}"


def summaryRanges(nums: list[int]) -> list[str]:
    if not nums:
        return []

    result = []
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            result.append(get_interval(start, nums[i - 1]))
            start = nums[i]
    result.append(get_interval(start, nums[-1]))
    return result


print(
    summaryRanges([1, 2, 3, 4, 6, 7, 9, 11])
)
