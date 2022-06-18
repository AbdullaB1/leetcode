from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.generate(n, 0, 0, [])
        return list(map(lambda x: "".join(x), self.result))

    def generate(self, n: int, opened: int, closed: int, current: List[str]) -> List[str]:
        # print(current)
        if opened == n and closed == n:
            self.result.append(current)
            return
        if opened < n:
            self.generate(n, opened + 1, closed, current + ["("])
        # закрытых скобок всегда должно быть столько же либо меньше, чем открывающих
        if closed < opened:
            self.generate(n, opened, closed + 1, current + [")"])
