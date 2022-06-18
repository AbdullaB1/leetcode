from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.backtrack(n, k, 1, [])
        return self.result

    def backtrack(self, n: int, k: int, current: int, path: list[int]) -> List[List[int]]:
        if len(path) == k:
            self.result.append(path)

        for i in range(current, n + 1):
            self.backtrack(n, k, i + 1, path + [i])
