from collections import defaultdict

# решение Саши Лапина


def solution_1(mas, s):
    dct = {}
    min_len = len(s)
    result = s
    # создал словарь со значениями
    for i in mas:
        dct[i] = 0
    correct = len(dct)
    # указатель
    pointer = 0
    for i in range(len(s)):
        if s[i] in dct:
            dct[s[i]] += 1
            if dct[s[i]] == 1:
                correct -= 1
        # нет необходимости в условии
        # i - pointer >= len(mas)
        # но оно написано не правильно
        # while correct == 0 and i - pointer >= len(mas):
        # без него все ок
        while correct == 0 and i - pointer >= len(mas) - 1:
            if i - pointer + 1 < min_len:
                min_len = i - pointer + 1
                result = s[pointer:i+1]
            if s[pointer] in dct:
                dct[s[pointer]] -= 1
                if dct[s[pointer]] == 0:
                    correct += 1
            pointer += 1
    return result


def solution(mas, s):
    chars = defaultdict(int, zip(mas, [0] * len(mas)))
    result = s
    correct = 0
    start = 0
    for i in range(len(s)):
        if s[i] in chars:
            chars[s[i]] += 1
            if chars[s[i]] == 1:
                correct += 1
        while correct == len(mas):
            if i - start + 1 < len(result):
                result = s[start: i + 1]
            if s[start] in chars:
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    correct -= 1
            start += 1
    return result


assert solution(['a', 'b', 'c'], "aaaadabc") == "abc"
assert solution(['a', 'b', 'c'], "aabbc") == "abbc"
assert solution(['a', 'b', 'c'], "fffafbfcfff") == "afbfc"
assert solution(['a', 'b', 'c'], "aabbccaabbcabc") == "bca"
# невозможно составить такую строку
assert solution(['a', 'b', 'c'], "ccccaaaafffff") == "ccccaaaafffff"
assert solution(['a', 'b', 'c'], "fffaaaabbbccccffff") == "abbbc"

print(
    solution(
        ['a', 'b', 'c'], "aaaadabc"
    )
)
