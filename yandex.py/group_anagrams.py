from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for word in strs:
            result[str(sorted(word))].append(word)
        return [words for words in result.values()]


s = Solution()
print(
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
)
