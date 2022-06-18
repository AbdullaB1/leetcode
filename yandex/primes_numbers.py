import math


# обычный способ
def first_n_primes(n: int) -> int:
    prevs = [2] if n >= 1 else []
    i = 3
    while len(prevs) < n:
        if i > 10 and i % 5 == 0:
            i += 2
            continue
        for j in prevs:
            if j * j - 1 > i:
                prevs.append(i)
                # yield i
                break
            if i % j == 0:
                break
        else:
            prevs.append(i)
            # yield i

        i += 2
    return prevs


# print(
#     *first_n_primes(100)
# )

# через решето эрастогена
def sieve_of_eratosthenes(n: int):
    a = [1] * (n + 1)
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(i)
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    print(lst)


# sieve_of_eratosthenes(100)


def f(n: int) -> list[int]:
    result = []
    arr = [1] * (n + 1)
    arr[1] = 0
    for i in range(2, n + 1, 1):
        if arr[i] != 0:
            result.append(i)
            for j in range(i, n + 1, i):
                arr[j] = 0
    print(result)


f(100)


def f2(n: int):
    res = [2]
    i = 3
    while len(res) < n:
        isqrt = int(math.sqrt(i) + 1)
        for j in res:
            if j > isqrt:
                res.append(i)
                break
            if i % j == 0:
                break
        else:
            res.append(i)
        i += 2
    return res


# f2(100000)
# print(
#     f2(100)
# )
