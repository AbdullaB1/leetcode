class Solution:
    def climbStairs(self, n: int) -> int:
        # по сути это числа фибоначи
        if n == 1:
            return 1
        if n == 2:
            return 2
        n_1 = 1
        n_2 = 2
        for i in range(3, n + 1):
            n_1, n_2 = n_2, n_1 + n_2
        return n_2

        # res_list = [0] * (n + 1)
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # res_list[1] = 1
        # res_list[2] = 2
        # i = 3
        # while i <= n:
        #     res_list[i] = res_list[i - 1] + res_list[i - 2]
        #     i += 1
        # return res_list[n]


#         from functools import lru_cache


#         @lru_cache
#         def variant_count(n: int) -> int:
#             if n == 1:
#                 return 1
#             elif n == 2:
#                 return 2
#             else:
#                 return variant_count(n - 1) + variant_count(n - 2)

#         return variant_count(n)
