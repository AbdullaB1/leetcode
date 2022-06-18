class Solution:
    def countBits(self, n: int) -> list[int]:
        memo = [0] * (n + 1)
        for i in range(1, n + 1):
            memo[i] = memo[i // 2] + i % 2
        return memo

        # size = math.ceil(math.log(n + 1, 2))
        # result = [0]
        # for i in range(1, n + 1):
        #     cur = 0
        #     for j in range(size):
        #         r = i % (2**(j + 1)) >= 2**j
        #         cur += int(r)
        #     result.append(cur)
        # return result
