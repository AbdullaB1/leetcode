from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        elems = set(nums)
        for i in range(len(nums)):
            if nums[i] in elems:
                cur_seq = 1
                cur_el = nums[i]
                elems.remove(cur_el)
                while cur_el - 1 in elems:
                    cur_el -= 1
                    cur_seq += 1
                    elems.remove(cur_el)
                cur_el = nums[i]
                while cur_el + 1 in elems:
                    cur_el += 1
                    cur_seq += 1
                    elems.remove(cur_el)
                max_seq = max(max_seq, cur_seq)
        return max_seq
