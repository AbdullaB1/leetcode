from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            nums[abs(num) - 1] *= -1

        return result

        # index = 0
        # for i in range(len(nums)):
        #     while nums[i] != i + 1:
        #         val = nums[i]
        #         if nums[val - 1] == nums[i]:
        #             break
        #         nums[i], nums[val - 1] = nums[val - 1], nums[i]
        # # print(nums)
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] != i + 1:
        #         result.append(nums[i])
        # return result
