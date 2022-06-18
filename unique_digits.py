from typing import List


# одно из возможных простых решений

# https://www.geeksforgeeks.org/next-number-with-distinct-digits/

def countNumbersWithUniqueDigits(min_val: int, max_val: int) -> int:
    lenght = 1
    ost = min_val
    while ost // 10 > 0:
        lenght += 1
        ost //= 10
    print(lenght)
    res = 0
    while lenght:
        res *= 10
        res += 9
        lenght -= 1
    print(min_val, res)

    lenght = 0
    ost = max_val
    while ost // 10 > 0:
        lenght += 1
        ost //= 10
    print(lenght)
    res = 1
    while lenght:
        res *= 10
        lenght -= 1
    print(max_val, res)


countNumbersWithUniqueDigits(36, 3036)
