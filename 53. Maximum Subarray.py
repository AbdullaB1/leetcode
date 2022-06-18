class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

        # max_sum = nums[0]
        # cur_min = nums[0]
        # cur_sum = nums[0]
        # for num in nums:
        #     cur_sum += num
        #     max_sum = max(cur_sum - cur_min, max_sum)
        #     cur_min = min(cur_sum, cur_min)
        # return max_sum
