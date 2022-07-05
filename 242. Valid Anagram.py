from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        for c in t:
            if c not in s_counter:
                return False
            s_counter[c] -= 1
            if s_counter[c] == 0:
                s_counter.pop(c)
        return not s_counter
