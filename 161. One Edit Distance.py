# https://www.lintcode.com/problem/640/description


def is_strings_equal_after_one_change(first: str, second: str) -> bool:
    # если длины строк совпадают, значит подойдёт только замена символа
    if len(first) == len(second):
        diff = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                diff += 1
            if diff > 1:
                return False
        # если есть условие, что равные строки должны возвращать False
        if diff == 0:
            return False
    # если же длина строк различатеся, значит нужно удалить лишний символ в более длинной строке
    else:
        if abs(len(first) - len(second)) > 1:
            return False
        if len(second) > len(first):
            first, second = second, first
        diff = 0
        for i in range(len(second)):
            if first[i + diff] != second[i]:
                diff += 1
            if diff > 1:
                return False
    return True


def isOneEditDistance(first: str, second: str) -> bool:
    # удобней считать, что втрорая строка не короче первой
    if len(first) > len(second):
        first, second = second, first

    for i in range(len(first)):
        if first[i] != second[i]:
            if len(first) == len(second):
                return first[i + 1:] == second[i + 1:]
            return first[i:] == second[i + 1:]
    # если до этого не было ни одного несовпадения,
    # занчит нуно просто проверть, что вторая не слтшкмо длинная
    return len(second) - len(first) <= 1


def is_strings_equal_after_one_change(word1: str, word2: str) -> bool:
    if len(word1) == len(word2):
        # замена
        counter = 0
        for i, j in zip(word1, word2):
            if i != j:
                counter += 1
        if counter > 1:
            return False
        return True
    else:
        # добавление или удаление
        counter = 0
        p1, p2 = 0, 0
        while p1 < len(word1) and p2 < len(word2):
            print(word1[p1], word2[p2])
            if word1[p1] != word2[p2]:
                counter += 1
                if len(word1) > len(word2):
                    p1 += 1
                else:
                    p2 += 1
            else:
                p1 += 1
                p2 += 1
        counter += (max(len(word1), len(word2)) - max(p2, p1))
        if counter > 1:
            return False
        return True


assert is_strings_equal_after_one_change("", "") == True
assert is_strings_equal_after_one_change("abcd", "abcd") == True
assert is_strings_equal_after_one_change("aacd", "abcd") == True
assert is_strings_equal_after_one_change("abcd", "accd") == True
assert is_strings_equal_after_one_change("abcd", "abbd") == True
assert is_strings_equal_after_one_change("abcd", "abcc") == True
assert is_strings_equal_after_one_change("abcde", "abccc") == False
assert is_strings_equal_after_one_change("abcde", "bbcdd") == False

assert is_strings_equal_after_one_change("", "a") == True
assert is_strings_equal_after_one_change("a", "ab") == True
assert is_strings_equal_after_one_change("abcd", "abcde") == True
assert is_strings_equal_after_one_change("abcd", "abced") == True
assert is_strings_equal_after_one_change("abcd", "abecd") == True
assert is_strings_equal_after_one_change("abcd", "aebcd") == True
assert is_strings_equal_after_one_change("abcd", "eabcd") == True
assert is_strings_equal_after_one_change("abcd", "abcdef") == False
assert is_strings_equal_after_one_change("abcd", "aacde") == False

print(
    is_strings_equal_after_one_change(
        "abcd", "abced"
    )
)


# реализация на литкоде
class Solution:
    # slice возвращает копию строки, поэтому возмодно по памяти будет выгодней странивать строки так
    # как минниму стоит спросить про это интервьюера
    def isOneEditDistance(self, s: str, t: str) -> bool:
        def strEqual(s: str, si: int, t: str, ti: int) -> bool:
            if len(s) - si != len(t) - ti:
                return False
            while si < len(s) and ti < len(t):
                if s[si] != t[ti]:
                    return False
                si += 1
                ti += 1
            return True

        n = len(s)
        m = len(t)
        if n > m:
            n, m = m, n
            s, t = t, s
        for i in range(n):
            if s[i] != t[i]:
                if m > n:
                    # s[i:] == t[i + 1:]
                    return strEqual(s, i, t, i + 1)
                else:
                    # s[i + 1:] == t[i + 1:]
                    return strEqual(s, i + 1, t, i + 1)
        return m - n == 1
