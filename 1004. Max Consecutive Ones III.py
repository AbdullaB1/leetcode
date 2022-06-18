from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_seq = zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_seq = max(max_seq, right - left + 1)
        return max_seq
