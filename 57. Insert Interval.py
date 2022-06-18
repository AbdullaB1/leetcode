from typing import List


class Solution:
    # решение литокода
    # так как нам все равно нужно вернуть измененный массив, то просто пройдесмя по нему,
    # и вставим в нужное место новый интервал
    # попутно будем мерджить необходимые интервалы к новому
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        if result and result[-1][1] >= newInterval[0]:
            result[-1][1] = max(result[-1][1], newInterval[1])
        else:
            result.append(newInterval)

        while i < len(intervals):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1

        return result

    # попытка съекономить на поиске нужного для вставки элемента
    # но на скорость не влияет, так как в итоге все равно придется все скопировать в новый массив

    def insert_1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        left = self.search_first_overlap(
            intervals, newInterval
        )
        right = self.search_last_overlap(
            intervals, newInterval
        )
        # значит нашлось старые интервалы, которые нужно будет слить с новым
        # но если в массиве 1 элемент или его нужно вставить в конец или начало старого,
        # то left и right будут равны, поэтому нужно написать дополнительное условие
        if left <= right and intervals[left][1] >= newInterval[0] and intervals[left][0] <= newInterval[1]:
            merged = (
                min(intervals[left][0], newInterval[0]),
                max(intervals[right][1], newInterval[1])
            )
            intervals[left:right + 1] = [merged]
        # если индексы сопали, но это оказалось только потому,
        # что новый интервал нужно вставить перед или после старого массива интервалов,
        # то птыаемся понять, куда же его вставить
        elif intervals[right][1] < newInterval[0]:
            intervals[right:right + 1] = [intervals[right], newInterval]
        else:
            intervals[left:left + 1] = [newInterval, intervals[left]]
        return intervals

    def search_first_overlap(self, intervals: List[List[int]], newInterval: List[int]) -> int:
        l = 0
        r = len(intervals) - 1
        target = newInterval[0]
        while l < r:
            mid = (l + r) // 2
            if intervals[mid][1] >= target:
                r = mid
            else:
                l = mid + 1
        return l

    def search_last_overlap(self, intervals: List[List[int]], newInterval: List[int]) -> int:
        l = 0
        r = len(intervals) - 1
        target = newInterval[1]
        while l < r:
            mid = (l + r + 1) // 2
            if intervals[mid][0] <= target:
                l = mid
            else:
                r = mid - 1
        return l
