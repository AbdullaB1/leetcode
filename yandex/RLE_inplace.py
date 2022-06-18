class Solution:
    def compress_char(self, chars: list[str], first: int, char: int, count: int) -> int:
        chars[first] = char
        first += 1
        if count > 1:
            for c in str(count):
                chars[first] = c
                first += 1
        return first

    def compress(self, chars: list[str]) -> int:
        first = 0
        count = 1
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                first = self.compress_char(chars, first, chars[i - 1], count)
                count = 1
            else:
                count += 1
        first = self.compress_char(chars, first, chars[-1], count)
        return first
