class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

        # nums_set = set()
        # for num in nums:
        #     if num in nums_set:
        #         nums_set.remove(num)
        #     else:
        #         nums_set.add(num)
        # return list(nums_set)[0]
