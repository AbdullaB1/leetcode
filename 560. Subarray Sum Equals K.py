from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefs_set = defaultdict(int, {0: 1})
        # prefs_set[0] = 1
        # вместо подсчета префикс сум заранне, можно делать это на лету
        cursum = 0
        for num in nums:
            cursum += num
            if cursum - k in prefs_set:
                result += prefs_set[cursum - k]
            prefs_set[cursum] += 1

        return result

    def subarraySum_1(self, nums: List[int], k: int) -> int:
        result = 0
        prefs = [0]
        for i in range(len(nums)):
            prefs.append(prefs[-1] + nums[i])

        prefs_set = defaultdict(int)
        for pref in prefs:
            if pref - k in prefs_set:
                result += prefs_set[pref - k]
            prefs_set[pref] += 1

        return result
