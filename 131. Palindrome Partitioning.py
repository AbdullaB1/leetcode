from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.results = []
        self.cache = {(i, i): True for i in range(len(s))}
        self.generate(s, 0, [])
        # print(self.cache)
        return self.results

    def generate(self, s: str, start: int, path: List[str]) -> List[List[str]]:
        if start >= len(s):
            self.results.append(path)
        for i in range(start, len(s)):
            if self.isPalindrom(s, start, i):
                self.generate(s, i + 1, path + [s[start:i + 1]])

    def isPalindrom(self, s: str, left: int, right: int) -> bool:
        l = left
        r = right
        while l <= r:
            if (l, r) in self.cache:
                self.cache[(left, right)] = self.cache[(l, r)]
                return self.cache[(l, r)]

            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                self.cache[(left, right)] = False
                return False
        self.cache[(left, right)] = True
        return True
