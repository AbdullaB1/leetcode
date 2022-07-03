from collections import defaultdict
from collections import Counter


class Solution:
    # очень короткое решение Вовы
    def find_anagrams(s: str, p: str):
        ans = []
        count = Counter(p)
        n = len(p)
        required = n

        for r, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                required -= 1
            if r >= n:
                count[s[r - n]] += 1
                if count[s[r - n]] > 0:
                    required += 1
            if required == 0:
                ans.append(r - n + 1)

        return ans

    # решение после прозрения

    def findAnagrams(self, source, target):
        if len(source) < len(target):
            return []
        result = []
        chars = defaultdict(int)
        for c in target:
            chars[c] += 1
        for i in range(len(target)):
            chars[source[i]] -= 1
            if chars[source[i]] == 0:
                chars.pop(source[i])
        if not chars:
            result.append(0)
        for i in range(len(source) - len(target)):
            addc = source[i + len(target)]
            remc = source[i]
            chars[addc] -= 1
            if chars[addc] == 0:
                chars.pop(addc)
            chars[remc] += 1
            if chars[remc] == 0:
                chars.pop(remc)
            if not chars:
                result.append(i + 1)
        return result


class Solution:
    # старое запутанное решение
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


class Solution:
    """укороченное решение"""

    def findAnagrams(self, source: str, target: str) -> list[int]:
        if len(source) < len(target):
            return []
        result = []
        chars = defaultdict(int, Counter(target))
        for i in range(len(source)):
            if i >= len(target):
                addc = source[i - len(target)]
                chars[addc] -= 1
                if chars[addc] == 0:
                    chars.pop(addc)
            remc = source[i]
            chars[remc] += 1
            if chars[remc] == 0:
                chars.pop(remc)
            if not chars:
                result.append(i - len(target) + 1)
        return result


print(Solution().findAnagrams(
    "cbaebabacd",
    "abc",
))
