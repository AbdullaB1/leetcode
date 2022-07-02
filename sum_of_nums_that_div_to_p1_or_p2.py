"""
Найти сумму чисел, которые делятся на p1 либо на p2 и меньше n
:param n: Число сумму до какого нужно посчитать
:param p1: делитель номер 1
:param p2: делитель номер 2
:return:
p1_count (p1_count + 1 ) //2 
"""


def sum_by_params_my(n: int, p1: int, p2: int):
    result = 0
    p1_count = (n - 1) // p1
    p2_count = (n - 1) // p2
    result += (p1_count * p1 + p1) * p1_count // 2
    result += (p2_count * p2 + p2) * p2_count // 2
    p3 = p1 * p2
    p3_count = (n - 1) // p3
    result -= (p3_count * p3 + p3) * p3_count // 2
    return result


# по сути тоже самое, но немного по другому
def sum_by_params(n: int, p1: int, p2: int) -> int:
    ap1 = (n - 1) // p1
    sp1 = ((ap1 + 1) * ap1 // 2) * p1

    ap2 = (n - 1) // p2
    sp2 = ((ap2 + 1) * ap2 // 2) * p2

    ap1p2 = (n-1) // (p1*p2)
    sp1p2 = ((ap1p2 + 1) * ap1p2 // 2) * p1 * p2

    result = sp1 + sp2 - sp1p2
    return result


assert sum_by_params(30, 3, 5) == 195
