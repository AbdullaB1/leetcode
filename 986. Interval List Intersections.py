from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        result = []

        while first < len(firstList) and second < len(secondList):
            max_begin = max(firstList[first][0], secondList[second][0])
            min_end = min(firstList[first][1], secondList[second][1])

            if min_end >= max_begin:
                result.append([max_begin, min_end])

            # важно перемещать по конце отрезка, а не по началу,
            # так как отрезок с более дальним концом может захватить сразу несколько
            # отрезков другой последовательности
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1

        return result


class Solution:
    """тоже рабочее решение, но с немного более сложным условием"""

    def intervalIntersection(self, first: list[list[int]], second: list[list[int]]) -> list[list[int]]:
        p1 = 0
        p2 = 0
        result = []
        while p1 < len(first) and p2 < len(second):
            if (first[p1][0] <= second[p2][0] <= first[p1][1]) or (second[p2][0] <= first[p1][0] <= second[p2][1]):
                result.append(
                    [
                        max(first[p1][0], second[p2][0]),
                        min(first[p1][1], second[p2][1]),
                    ]
                )
            if first[p1][1] < second[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return result


print(Solution().intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]],
    [[1, 5], [8, 12], [15, 24], [25, 26]],
))
