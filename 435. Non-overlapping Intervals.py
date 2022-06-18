from typing import List


class Solution:
    # много рещениний
    # это показалось самым понятным
    # если встретили пересечение множест, откинули то,
    # у которого конец находится дальше,
    # так как более длинный конец потенциально может зацепить большее количесво соседей
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        prev = (intervals[0])
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                result += 1
                prev = min(prev, intervals[i], key=lambda x: x[1])
            else:
                prev = intervals[i]
        return result
