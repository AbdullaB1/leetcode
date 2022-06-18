from typing import List
import heapq


class Solution:
    # через очередь с приоритетом
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        max_rooms = 0
        intervals.sort()
        for inter in intervals:
            while rooms and rooms[0] <= inter[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, inter[1])
            max_rooms = max(max_rooms, len(rooms))
        return max_rooms

    # через прибавление к текущему коичеству комнат 1, если комнату заняли,
    # и вычитание 1, если команта освободилась

    def minMeetingRooms_1(self, intervals: List[List[int]]) -> int:
        actions = []
        for interval in intervals:
            actions.append((interval[0], 1))
            actions.append((interval[1], -1))
        actions.sort()
        max_rooms = 0
        current = 0
        for a in actions:
            current += a[1]
            max_rooms = max(max_rooms, current)
        return max_rooms
