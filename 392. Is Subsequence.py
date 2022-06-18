class Solution:
    def isSubsequence(self, source: str, target: str) -> bool:
        s = 0
        for t in target:
            if s == len(source):
                return True
            if t == source[s]:
                s += 1
        return s == len(source)


s = Solution()
print(
    s.isSubsequence("abc", "adfvsdfvsdfvabadcasvfdvfdvc")
)
