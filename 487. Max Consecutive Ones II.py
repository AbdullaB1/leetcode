from typing import List


class Solution:

    # мне нарвится больше это решение
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        max_seq = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prev = curr
                curr = 0
            else:
                curr += 1
            max_seq = max(max_seq, prev + curr)
        if max_seq == len(nums):
            return max_seq
        return max_seq + 1

    def findMaxConsecutiveOnes_1(self, nums: List[int]) -> int:
        # можно проверять макимум только при появлении нулей и в конце, в не все время
        prev = 0
        curr = 0
        max_seq = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_seq = max(max_seq, prev + curr)
                prev = curr
                curr = 0
            else:
                curr += 1
        max_seq = max(max_seq, prev + curr)
        if max_seq == len(nums):
            return max_seq
        return max_seq + 1

    def findMaxConsecutiveOnes_2(self, nums: List[int]) -> int:
        left = max_seq = zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_seq = max(max_seq, right - left + 1)
        return max_seq
