def urlify(s: list[str]) -> list[str]:
    space_cnt = 0
    idx = len(s) - 1
    for c in s:
        if c == " ":
            space_cnt += 1
    s.extend([" " for _ in range(space_cnt * 2)])
    end_idx = len(s) - 1
    while idx >= 0:
        if s[idx] == " ":
            # нужно уточнить сложность
            # s[end_idx - 2: end_idx + 1] = "%20"
            s[end_idx] = "0"
            s[end_idx - 1] = "2"
            s[end_idx - 2] = "%"
            end_idx -= 3
        else:
            s[end_idx] = s[idx]
            end_idx -= 1
        idx -= 1
    return s

print("".join(urlify(list("hello, world!"))))
assert "".join(urlify(list("hello, world!"))) == "hello, world!".replace(" ", "%20")
assert "".join(urlify(list("  hello, world!"))) == "  hello, world!".replace(" ", "%20")
assert "".join(urlify(list("hello, world!  "))) == "hello, world!  ".replace(" ", "%20")
assert "".join(urlify(list("  hello, world!  "))) == "  hello, world!  ".replace(" ", "%20")
assert "".join(urlify(list(" hello,  world! "))) == " hello,  world! ".replace(" ", "%20")
