from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.backtrack(candidates, target, 0, [], 0)
        return self.results

    def backtrack(self, candidates: List[int], target: int, index: int, current: List[int], cursum: int) -> None:
        if cursum > target:
            return

        if cursum == target:
            self.results.append(current[:])
            return

        for i in range(index, len(candidates)):
            num = candidates[i]
            current.append(num)
            self.backtrack(candidates, target, i, current, cursum + num)
            current.pop()


class Solution_1:
    # в этом способе потребляется немноо меньще памяти, но на скорость в литкоде не повлияло
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.backtrack(candidates, target, 0, [], 0)
        return self.results

    def backtrack(self, candidates: List[int], target: int, index: int, current: List[int], cursum: int) -> None:
        if cursum > target:
            return

        if cursum == target:
            self.results.append(current)
            return

        for i in range(index, len(candidates)):
            num = candidates[i]
            self.backtrack(candidates, target, i,
                           current + [num], cursum + num)
