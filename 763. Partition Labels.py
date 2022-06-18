from typing import List
import math
from collections import defaultdict


class Solution:
    # O(n)
    # решение, придложенное литкодом
    # мы сразу записываем ответ, без сохранения интервалов
    # вместо этого мы постоянно поддерживаем корректные начало и конец текущего отрезка
    def partitionLabels(self, s: str) -> List[int]:
        letters = {c: i for i, c in enumerate(s)}
        results = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, letters[c])
            if i == end:
                results.append(end - start + 1)
                start = i + 1

        return results

    # O(n)
    # решение, прищедшее мне в голову
    def partitionLabels_1(self, s: str) -> List[int]:
        letters = {c: i for i, c in enumerate(s)}
        results = []

        for i, c in enumerate(s):
            if results and results[-1][1] >= i:
                results[-1][1] = max(results[-1][1], letters[c])
            else:
                results.append([i, letters[c]])

        return list(map(lambda x: x[1] - x[0] + 1, results))

    # O(n log n)

    def partitionLabels_2(self, s: str) -> List[int]:
        letters = defaultdict(lambda: [math.inf, -math.inf])
        for i, c in enumerate(s):
            if i < letters[c][0]:
                letters[c][0] = i
            if i > letters[c][1]:
                letters[c][1] = i
        inters = sorted(letters.values())
        result = []
        for inter in inters:
            if result and result[-1][1] >= inter[0]:
                result[-1][1] = max(result[-1][1], inter[1])
            else:
                result.append(inter)
        return list(map(lambda x: x[1] - x[0] + 1, result))
