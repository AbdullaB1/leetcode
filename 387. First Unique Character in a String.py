from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = defaultdict(lambda: [0, 0])
        for i, c in enumerate(s):
            if c not in chars:
                chars[c][0] = i
                chars[c][1] = 1
            else:
                chars[c][1] += 1
        # по умолчанию ключи в словаре хранятся в порядке добавления
        # поэтому первое же совпадение будет являться ответом
        for key in chars:
            if chars[key][1] == 1:
                return chars[key][0]
        return -1
