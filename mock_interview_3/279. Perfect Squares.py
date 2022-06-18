import math


class Solution:
    # математическое решение
    # любое число можно разложить на сумму 4 квадратов,
    # и есть формула, позволяющая узнать, есть ли способ легче
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq*sq == n

    def numSquares(self, n: int) -> int:
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7:  # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3

    # через обход в ширину
    def numSquares_4(self, n: int) -> int:
        variants = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        queue = {n}
        for i in range(1, n + 1):
            # важно сохранять результаты каждой операции в set,
            # так как иначе одни и те результаты будут просчитываться многократно
            next_queue = set()
            for _ in range(len(queue)):
                n = queue.pop()
                for v in variants:
                    if n - v == 0:
                        return i
                    if n - v < 0:
                        continue
                    next_queue.add(n - v)
            queue = next_queue

    # работатет очень быстро
    def numSquares_3(self, n: int) -> int:
        def isDividedBy(n: int, by: int) -> bool:
            if by == 1:
                return n in variants
            if n < 0:
                return False
            for v in variants:
                if isDividedBy(n - v, by - 1):
                    return True

        variants = [i * i for i in range(1, int(math.sqrt(n)) + 1)][::-1]
        for i in range(1, n + 1):
            if isDividedBy(n, i):
                return i

    # падает на 6366

    def numSquares_2(self, n: int) -> int:
        self.variants = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        self.cache = [-1] * (n + 1)
        self.cache[0] = 0
        return self.travers(n)

    def travers(self, n: int) -> int:
        if self.cache[n] >= 0:
            return self.cache[n]
        if n < 0:
            return math.inf
        self.cache[n] = min(
            map(lambda x: self.travers(n - x), self.variants)
        ) + 1
        return self.cache[n]

    # через динамическое программирование
    # O( N * sqrt(N) )
    def numSquares_1(self, n: int) -> int:
        result = 0
        variants = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        memo = [math.inf] * (n + 1)
        memo[0] = 0
        for v in variants:
            memo[v] = 1
        for i in range(1, len(memo)):
            for v in variants:
                if i - v >= 0:
                    memo[i] = min(memo[i], memo[i - v] + 1)
        return memo[n]
