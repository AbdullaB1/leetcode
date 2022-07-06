from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = deque()
        result = []
        for i, num in enumerate(nums):
            while maxes and maxes[-1] < num:
                maxes.pop()
            maxes.append(num)

            if i >= k and maxes[0] == nums[i - k]:
                maxes.popleft()

            if i >= k - 1:
                result.append(maxes[0])
        return result


class Solution:
    """похожее решение, но для удаления из дека пользуемся индексами в массиве"""
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = deque()
        result = []
        for i, num in enumerate(nums):
            while maxes and num > maxes[-1][1]:
                maxes.pop()
            maxes.append([i, num])
            if i >= k - 1:
                result.append(maxes[0][1])
            if i >= k - 1 and maxes[0][0] <= i - k + 1:
                maxes.popleft()
        return result


s = Solution()
print(
    s.maxSlidingWindow(
        [3, 2, 1, 5, 6, 7, 5, 4],
        3
    )
)
