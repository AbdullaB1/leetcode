class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num1 = 0
        m = 1
        for i in range(len(firstWord) - 1, -1, -1):
            num1 += m * (ord(firstWord[i]) - ord('a'))
            m *= 10
        num2 = 0
        m = 1
        for i in range(len(secondWord) - 1, -1, -1):
            num2 += m * (ord(secondWord[i]) - ord('a'))
            m *= 10
        num3 = 0
        m = 1
        for i in range(len(targetWord) - 1, -1, -1):
            num3 += m * (ord(targetWord[i]) - ord('a'))
            m *= 10
        return num1 + num2 == num3
