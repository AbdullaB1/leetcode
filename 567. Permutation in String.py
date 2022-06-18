from typing import DefaultDict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = DefaultDict(int)
        for c in s1:
            counter[c] += 1

        for i in range(len(s1)):
            counter[s2[i]] -= 1
            if counter[s2[i]] == 0:
                counter.pop(s2[i])

        if not counter:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            for_del = i - 1
            for_add = i + len(s1) - 1

            counter[s2[for_del]] += 1
            if counter[s2[for_del]] == 0:
                counter.pop(s2[for_del])

            counter[s2[for_add]] -= 1
            if counter[s2[for_add]] == 0:
                counter.pop(s2[for_add])

            if not counter:
                return True
        return False
