class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = 0
        mul = 1
        for i in range(len(num1) - 1, -1, -1):
            result += mul * (ord(num1[i]) - ord('0'))
            mul *= 10
        mul = 1
        for i in range(len(num2) - 1, -1, -1):
            result += mul * (ord(num2[i]) - ord('0'))
            mul *= 10
        return str(result)


s = Solution()
print(
    s.addStrings(
        "123", "44"
    )
)
