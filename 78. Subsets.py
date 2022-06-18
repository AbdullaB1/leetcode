from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # через добавление ко всем предыдущим вариантам нового числа
        result = [[]]

        for num in nums:
            result.extend(
                [res + [num] for res in result]
            )

        return result

        # через степени двойки
#         result = []

#         for i in range(2 ** len(nums)):
#             cur = []
#             for j in range(len(nums)):
#                 if i & 2 ** j != 0:
#                     cur.append(nums[j])
#             result.append(cur)

#         return result
