class Solution:
    # не получилось решить через динамическое программирование
    # это решение без использоваиня доп памятиф
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s) - 1):
            res1 = self.palAroundCenter(s, i, i)
            res2 = self.palAroundCenter(s, i, i + 1)
            if res1 * 2 - 1 > end - start + 1:
                start = i - res1 + 1
                end = i + res1 - 1
            if res2 * 2 > end - start + 1:
                start = i - res2 + 1
                end = i + res2
        return s[start:end + 1]

    def palAroundCenter(self, s: str, l: int, r: int) -> bool:
        lenght = 0
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                lenght += 1
            else:
                break
            l -= 1
            r += 1
        return lenght
