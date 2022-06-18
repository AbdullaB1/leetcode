from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        chars = defaultdict(int)
        start = 0
        max_seq = 0
        for i, c in enumerate(s):
            chars[c] += 1
            while len(chars) > 2:
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    chars.pop(s[start])
                start += 1
            max_seq = max(max_seq, i - start + 1)
        return max_seq


s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("eceba"))
