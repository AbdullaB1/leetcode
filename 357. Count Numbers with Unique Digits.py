from typing import List


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        self.result = 0
        self.nums = []
        self.travers(n, 0, [False for _ in range(10)])
        # print(self.nums)
        return self.result

    def travers(self, n: int, curr: int, used: List[bool]) -> None:
        if curr <= n:
            self.result += 1
            # self.nums.append([i for i in range(10) if used[i]])
        if curr >= n:
            return
        for i in range(10):
            if not used[i] and not (curr == 0 and i == 0):
                used[i] = True
                self.travers(n, curr + 1, used)
                used[i] = False


# вместо массива set, для отслеживания уже использованных цифр
class Solution_1:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        self.result = 0
        self.nums = []
        self.travers(n, 0, set())
        # print(self.nums)
        return self.result

    def travers(self, n: int, curr: int, used: set) -> None:
        if curr <= n:
            self.result += 1
            # self.nums.append([i for i in range(10) if used[i]])
        if curr >= n:
            return
        for i in range(10):
            if i not in used and not (curr == 0 and i == 0):
                used.add(i)
                self.travers(n, curr + 1, used)
                used.remove(i)
