from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        pers_count = [0] * (n + 1)
        for p1, p2 in trust:
            pers_count[p1] -= 1
            pers_count[p2] += 1

        # candidates = []
        for i in range(1, n + 1):
            if pers_count[i] == n - 1:
                return i

        # кандидатов будет не больше 1, тк пары индивидуальны, а значит случая,
        # в котором есть 2 судьи не произойдет, тк все долдны верить кому-то одному,
        # а судьи не могут никотму верить, получаем противоречие
        # if len(candidates) == 1:
        #     return candidates[0]

        return -1

    def findJudge_1(self, n: int, trust: List[List[int]]) -> int:
        who_trust = list(range(1, n + 1))
        trust_counts = defaultdict(int)
        for p1, p2 in trust:
            if p1 in who_trust:
                who_trust.remove(p1)
            trust_counts[p2] += 1
        if len(who_trust) == 1:
            if trust_counts[next(iter(who_trust))] == n - 1:
                return who_trust.pop()
        return -1
