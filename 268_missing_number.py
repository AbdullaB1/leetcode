# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


def missingNumber(nums: list[int]) -> int:
    res = 0
    n = len(nums)
    for i in range(n):
        res ^= i
        res ^= nums[i]
        print(res)
    i = n
    return res ^ i


print(
    missingNumber(list(map(int, input().split())))
)
