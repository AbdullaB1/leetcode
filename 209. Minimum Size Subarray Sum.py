class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = len(nums) + 1
        left = 0
        left_sum = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - left_sum >= target:
                while cur_sum - left_sum >= target:
                    min_len = min(min_len, i - left + 1)
                    left_sum += nums[left]
                    left += 1
        if min_len <= len(nums):
            return min_len
        return 0
