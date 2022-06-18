from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = []
        val = 0
        for i in range(n):
            maxV = 0
            while queue and queue[0][1] + k < i:
                heapq.heappop(queue)
            if queue:
                maxV = queue[0][0]
            val = nums[i] + (-1) * maxV
            heapq.heappush(queue, [-1 * val, i])
        return val

    def maxResult_1(self, nums: List[int], k: int) -> int:
        # O(N * K) Time Limit
        self.memo = [None] * len(nums)
        import math

        def max_result_recurently(nums: List[int], l: int, r: int, k: int) -> int:
            if self.memo[l] is not None:
                return self.memo[l]
            if r - l + 1 < 3 or k == 1:
                # print(nums, k, sum(nums[l: r + 1]), l, r)
                res = 0
                for i in range(l, r + 1):
                    res += nums[i]
                # res = sum(nums[l: r + 1])
                self.memo[l] = res
                return res
            else:
                curr_max = -math.inf
                for i in range(1, k + 1):
                    if l + i <= len(nums) - 1:
                        curr_max = max(
                            curr_max,
                            max_result_recurently(
                                nums, l + i, len(nums) - 1, k) + nums[l]
                        )

                # print(nums, k, curr_max, l, r)
                self.memo[l] = curr_max
                return curr_max

        return max_result_recurently(nums, 0, len(nums) - 1, k)


s = Solution()
print(
    s.maxResult(
        # [-4784, 1550, 2745, -5316],
        [1, -1, -2, 4, -7, 3],
        2
    )
)
