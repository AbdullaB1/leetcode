from typing import List
from collections import Counter


class Solution:
    # работает 4 раза быстрее второго рещения
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.perm_len = len(nums)
        self.backtrack([], Counter(nums))
        return self.result

    def backtrack(self, nums: List[int], counter) -> List[List[int]]:
        if len(nums) == self.perm_len:
            self.result.append(nums)
            return

        for key in counter:
            if counter[key] > 0:
                counter[key] -= 1
                self.backtrack(nums + [key], counter)
                counter[key] += 1


class Solution_1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        nums.sort()
        self.backtrack(nums, 0)
        return self.result

    def backtrack(self, nums: List[int], current: int) -> List[List[int]]:
        if current == len(nums) - 1:
            self.result.add(tuple(nums[:]))
            return

        for i in range(current, len(nums)):
            nums[current], nums[i] = nums[i], nums[current]
            self.backtrack(nums, current + 1)
            nums[current], nums[i] = nums[i], nums[current]


s = Solution()
print(
    s.permuteUnique(
        [1, 1, 2]
    )
)
