class Solution:
    def isSubsequence(self, sub: str, big: str) -> bool:
        idx = 0
        for c in big:
            if idx == len(sub):
                return True
            if c == sub[idx]:
                idx += 1
        return idx == len(sub)


s = Solution()
print(
    s.isSubsequence("abc", "ahbgdc")
)
