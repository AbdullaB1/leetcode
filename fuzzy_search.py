def fuzzy(source: str, target: str) -> bool:
    curr = 0
    for s in source:
        if curr >= len(target):
            return True
        elif s == target[curr]:
            curr += 1
    return curr >= len(target)


assert fuzzy("", "") == True
assert fuzzy("sdfvdsfvgsr", "") == True
assert fuzzy("", "d") == False
assert fuzzy("affffbfffc", "abc") == True
assert fuzzy("fffaffffbfffc", "abc") == True
assert fuzzy("affffbfffcfff", "abc") == True
assert fuzzy("affffbcfff", "abc") == True
assert fuzzy("aaaaffffbaabfffcbbbcfff", "abc") == True
