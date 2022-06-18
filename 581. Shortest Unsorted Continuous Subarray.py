import math
from typing import List


class Solution:
    # немного улучшенное решение из Solution
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mini = math.inf
        maxi = -math.inf

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:  # i элемент меньше предыдущего
                mini = min(mini, nums[i])  # найдем минимальный среди таких

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:  # аналогично ищем i который больше следующего
                maxi = max(maxi, nums[i])  # максимальный из таких

        # ищем первый больший нашего mini (минимальный не на своем месте)
        for l in range(len(nums)):
            if nums[l] > mini:
                break
        # например массив 1 2 3 7 5 6 8 9, mini = 5, maxi = 7, l - левая граница будет где семерка

        # ищем первый меньший нашего maxi (максимальный не на своем месте)
        for r in range(len(nums) - 1, -1, -1):
            if nums[r] < maxi:
                break

        return 0 if l >= r else r - l + 1

    # неплохие решение из обсуждений
    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/904404/Python-O(n)-Time-O(1)-Space-clean

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        l = 1
        while l < n - 1 and nums[l] > nums[l - 1]:
            l += 1
        mn = min(nums[l:])

        r = n - 2
        while r >= 0 and nums[r] < nums[r + 1]:
            r -= 1
        mx = max(nums[r::-1])

        i = 0
        while i < n and nums[i] <= mn:
            i += 1

        j = n - 1
        while j >= 0 and nums[j] >= mx:
            j -= 1

        return j - i + 1 if j - i > 0 else 0


s = Solution()
print(
    s.findUnsortedSubarray(
        None,
        # [1]
        [1, 3, 5, 4, 2]
    )
)
