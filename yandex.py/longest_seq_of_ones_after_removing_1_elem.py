class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        prev = curr = result = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                prev = curr
                curr = 0
            result = max(result, prev + curr)

        if result == len(nums):
            result -= 1

        return result


def longest_subarray(arr: list[int]) -> int:
    i = j = 0
    k = 1
    while j < len(arr):
        if arr[j] == 0:
            k -= 1
        if k < 0:
            if arr[i] == 0:
                k += 1
            i += 1
        j += 1
    result = j - i - 1
    return result if result >= 0 else 0
