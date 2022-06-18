from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        wordlist = s.split()
        for i in range(len(wordlist)):
            curr = []
            for j in range(len(wordlist[i]) - 1, -1, -1):
                curr.append(wordlist[i][j])
            wordlist[i] = ''.join(curr)
        return ' '.join(wordlist)

    # более самописаное решение
    def reverseWords_1(self, s: str) -> str:
        strlist = list(s)
        l = 0
        for i in range(len(strlist)):
            if strlist[i] == ' ':
                self.reverseOneWord(strlist, l, i - 1)
                l = i + 1
        self.reverseOneWord(strlist, l, len(strlist) - 1)
        return ''.join(strlist)

    def reverseOneWord(self, s: List[str], left: int, right: int) -> None:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s
