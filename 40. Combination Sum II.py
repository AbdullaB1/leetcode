from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        candidates.sort()
        print(candidates)
        self.backtrack(candidates, target, 0, [], 0)
        return self.results

    def backtrack(self, candidates: List[int], target: int, index: int, current: List[int], cursum: int) -> None:
        if cursum > target:
            return

        if cursum == target:
            self.results.append(current)
            return

        for i in range(index, len(candidates)):
            # не начинаем рекурсию от подряд идущих повторяющихся элементов
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            num = candidates[i]
            self.backtrack(candidates, target, i + 1,
                           current + [num], cursum + num)

# [1, 1, 2]
# [1]                   |  x  |  [2]
# [1, 1]    | [1, 2]    |          x
# [1, 1, 2] | x         |
# x         |           |
# [[1,1,2] [1, 1] [1, 2] [2]]
