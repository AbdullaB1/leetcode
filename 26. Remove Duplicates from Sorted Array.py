from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        first = 0
        for i in range(len(nums)):
            if nums[i] != prev:
                nums[first] = nums[i]
                prev = nums[i]
                first += 1
        return first
