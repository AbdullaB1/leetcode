import itertools
from typing import List


# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         return list(
#             map(
#                 lambda x: "".join(x),
#                 self.perm(list(s.lower()), 0)
#             )
#         )

#     def perm(self, s: List[str], index: int) -> List[str]:
#         for i in range(index, len(s)):
#             if not s[i].isdigit():
#                 lst1 = s[:]
#                 lst2 = s[:]
#                 lst2[i] = lst2[i].upper()
#                 res1 = self.perm(lst1, i + 1)
#                 res1.extend(self.perm(lst2, i + 1))
#                 return res1
#         return [s[:]]

# def letterCasePermutation(self, s: str) -> List[str]:
#     perms = [[0], [1]]
#     for_one = list(s.lower())
#     for_one[-1] = for_one[-1].upper()
#     result = {s.lower(), "".join(for_one)}
#     print(result)
#     # loop_val = math.ceil(math.log(len(s), 2))
#     for i in range(2, 2**len(s)):
#         cur = [c.lower() for c in s]
#         perm = perms[i // 2][:]
#         perm.append(i % 2)
#         print(perm)
#         perms.append(perm)
#         for i, p in enumerate(perm[::-1]):
#             if p == 1:
#                 cur[-i - 1] = cur[-i - 1].upper()
#         result.add("".join(cur))
#         print("".join(cur))
#     return list(result)

class Solution:
    # быстрее 85 процентов, работает быстрее рекурсивной версии
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [list(s)]

        for i in range(len(s)):
            if s[i].isalpha():
                for res in result:
                    cur = res[:]
                    cur[i] = cur[i].swapcase()
                    result.append(cur)

        return list(
            map(
                lambda x: "".join(x),
                result
            )
        )


# class Solution:
#     def letterCasePermutation(self, S: str) -> List[str]:
#         L = [set([i.lower(), i.upper()]) for i in S]
#         print(L)
#         return list(map(''.join, itertools.product(*L)))


s = Solution()
print(
    s.letterCasePermutation(
        "3z4"
    )
)
