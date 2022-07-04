from audioop import reverse
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


class Solution:
    """если бы пробелов могло быть неограниченное число"""
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        str_list = list(s)
        prev = ' '
        for i, c in enumerate(str_list):
            # если будут не только пробелы, можно использовать не c.isspace() 
            if prev == ' ' and c != ' ':
                start = i
            elif prev != ' ' and c == ' ':
                self.reverse_one_word(str_list, start, i - 1)
            prev = c
        if str_list[-1] != ' ':
            self.reverse_one_word(str_list, start, len(str_list) - 1)
        return ''.join(str_list)

    def reverse_one_word(self, s: List[str], left: int, right: int) -> None:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

print(Solution().reverse_words(
    "   Let's\t\t\ttake   LeetCode contest          ",
), "|")
