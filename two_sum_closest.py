def twoSumClosest(self, nums: list[int], l: int, r: int, target: int) -> int:
    """часть от задачи 3Sum, поедполагается, что l != r и l < r, l и r - корректные индексы массива nums"""
    start = l
    end = r
    result = nums[start] + nums[end]
    min_diff = abs(target - result)
    while start < end:
        curr = nums[start] + nums[end]
        if curr == target:
            return target
        elif curr < target:
            start += 1
        else:
            end -=1
        result, min_diff = min(
            (result, min_diff),
            (curr, abs(target - curr)),
            key=lambda x:x[1],
        )
    return result
