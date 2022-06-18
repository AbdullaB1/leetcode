from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map = defaultdict(lambda: [0, 0])
        for c in t:
            char_map[c][0] += 1

        count = 0
        min_len = len(s) + 1
        min_indexes = None
        left = right = 0
        right = -1
        while right < len(s):
            if count < len(char_map):
                right += 1
                if right >= len(s):
                    continue
                if s[right] in char_map:
                    if char_map[s[right]][0] <= char_map[s[right]][1]:
                        char_map[s[right]][1] += 1
                    else:
                        char_map[s[right]][1] += 1
                        if char_map[s[right]][0] == char_map[s[right]][1]:
                            count += 1
                continue

            while count == len(char_map):
                if s[left] in char_map:
                    if char_map[s[left]][0] < char_map[s[left]][1]:
                        char_map[s[left]][1] -= 1
                    else:
                        if char_map[s[left]][0] > char_map[s[left]][1] - 1:
                            if min_len > right - left + 1:
                                min_len = right - left + 1
                                min_indexes = (left, right)
                        char_map[s[left]][1] -= 1
                        count -= 1
                left += 1

        if not min_indexes:
            return ""
        return s[min_indexes[0]:min_indexes[1] + 1]
