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


#         first = 0
#         second = 0
#         result = []
#         while first < len(firstList) and second < len(secondList):
#             first_el = firstList[first]
#             second_el = secondList[second]
#             # print(first_el, second_el)
#             if first_el[0] <= second_el[0] <= first_el[1] or second_el[0] <= first_el[0] <= second_el[1]:
#                 result.append([
#                     max(first_el[0], second_el[0]),
#                     min(first_el[1], second_el[1])
#                 ])

#             if first_el[1] < second_el[1]:
#                 first += 1
#             else:
#                 second += 1

#         return result
