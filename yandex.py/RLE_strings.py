from itertools import groupby


def zip_str(c: str, counter: int) -> str:
    if counter == 1:
        return c
    else:
        return f"{c}{counter}"


def RLE(s: str) -> str:
    if not s:
        return ""
    result = []
    counter = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            result.append(zip_str(s[i - 1], counter))
            counter = 1
        else:
            counter += 1
    result.append(zip_str(s[-1], counter))
    return "".join(result)


# with itertools.groupby
def RLE_2(s: str) -> str:
    result = []
    for key, group in groupby(s):
        group_len = len(tuple(group))
        result.append(zip_str(key, group_len))
    return "".join(result)


print(
    # A4B3C2XYZD4E3F3A6B28
    RLE_2("AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB")
)
