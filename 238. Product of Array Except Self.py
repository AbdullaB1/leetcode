class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        cur = 1
        for num in nums:
            cur *= num
            result.append(cur)
        after = 1
        for i in range(len(result) - 1, -1, -1):
            before = result[i - 1] if i - 1 >= 0 else 1
            result[i] = after * before
            after *= nums[i]

        return result
