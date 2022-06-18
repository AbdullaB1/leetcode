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


s = Solution()
print(
    s.maxSlidingWindow(
        [3, 2, 1, 5, 6, 7, 5, 4],
        3
    )
)
