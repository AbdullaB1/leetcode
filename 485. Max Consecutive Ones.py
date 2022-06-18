from typing import List


class Solution:
    # более просто й и чаемый вариант
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        max_seq = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_seq = max(max_seq, curr)
                curr = 0
            else:
                curr += 1
        max_seq = max(max_seq, curr)
        return max_seq

    def findMaxConsecutiveOnes_1(self, nums: List[int]) -> int:
        curr = 0
        max_seq = 0
        prev = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if prev == 1:
                    max_seq = max(max_seq, curr)
                    curr = 0
            else:
                curr += 1
            prev = nums[i]
        max_seq = max(max_seq, curr)
        return max_seq
