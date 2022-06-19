from collections import defaultdict
import heapq


class Solution:
    def flatten(self, arr: list) -> list[int]:
        result = []
        stack = [arr]
        while stack:
            elem = stack.pop()
            if not isinstance(elem, list):
                result.append(elem)
            else:
                for i in range(len(elem) - 1, -1, -1):
                    stack.append(elem[i])
        return result


    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        tickets_dict = defaultdict(list)
        for t in tickets:
            heapq.heappush(tickets_dict[t[0]], t)
        return self.flatten(self.travers('JFK', tickets_dict))
        
    
    def travers(self, start: str, tickets_dict: dict[list[list[str, str]]]) -> list[str]:
        if not tickets_dict[start]:
            return [[start]]
        
        ticket = heapq.heappop(tickets_dict[start])
        result = self.travers(ticket[1], tickets_dict)
        if not tickets_dict[start]:
            return [[start] + result]
        ticket = heapq.heappop(tickets_dict[start])
        return [[start], self.travers(ticket[1], tickets_dict), result]
