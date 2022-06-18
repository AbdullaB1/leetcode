from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        start = 0
        res = 0
        for i, c in enumerate(s):
            chars[c] += 1
            while len(chars) > k:
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    chars.pop(s[start])
                start += 1
            res = max(res, i - start + 1)
        return res
