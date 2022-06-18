from collections import defaultdict


class Solution:
    def addchar(self, check_dict: dict[str, list], char: str, count: int) -> int:
        if char in check_dict:
            if check_dict[char][0] == check_dict[char][1]:
                check_dict[char][1] += 1
                count -= 1
            else:
                check_dict[char][1] += 1
                if check_dict[char][0] == check_dict[char][1]:
                    count += 1
        return count

    def remchar(self, check_dict: dict[str, list], char: str, count: int) -> int:
        if char in check_dict:
            if check_dict[char][0] == check_dict[char][1]:
                check_dict[char][1] -= 1
                count -= 1
            else:
                check_dict[char][1] -= 1
                if check_dict[char][0] == check_dict[char][1]:
                    count += 1
        return count

    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        check_dict = defaultdict(lambda: [0, 0])
        for c in p:
            check_dict[c][0] += 1

        count = 0

        for i in range(len(p)):
            count = self.addchar(check_dict, s[i], count)

        results = []
        if count == len(check_dict):
            results.append(0)

        for i in range(1, len(s) - len(p) + 1):
            prev = s[i - 1]
            curr = s[i + len(p) - 1]

            count = self.remchar(check_dict, prev, count)
            count = self.addchar(check_dict, curr, count)

            if count == len(check_dict):
                results.append(i)

        return results
