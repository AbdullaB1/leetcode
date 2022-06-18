from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            curr = nums[l] + nums[r]
            if curr == target:
                return [l + 1, r + 1]
            elif curr < target:
                l += 1
            else:
                r -= 1
        return []
