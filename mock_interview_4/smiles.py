def get_smiles(s: str) -> list[list[int]]:
    res = []
    for i in range(2, len(s)):
        c = s[i]
        if (c == "(" or c == ")") and s[i - 2] == ":" and s[i - 1] == "-":
            needed = c
            idx = i
            while idx + 1 < len(s) and s[idx + 1] == needed:
                idx += 1
            res.append((i, idx))
    return res


print(
    get_smiles(
        ":-)))))))))))))))))"
    )
)
