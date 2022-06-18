a = {
    'b': 4,
    'c': {
        'd': 3,
        'e': 5,
    }
}


def print_dict_1(d: dict) -> list[tuple[str, int]]:
    # не придется в дальнейшем проверять ключ на пустоту, так поолучались ответы вроде .d.c = 5
    stack = [*d.items()]
    result = []
    while stack:
        elem = stack.pop()
        if isinstance(elem[1], int):
            result.append((elem[0], elem[1]))
        else:
            for e in elem[1].items():
                cur_path = ".".join((elem[0], e[0]))
                stack.append((cur_path, e[1]))
    return result


def print_dict(d: dict, path: str = "") -> list:
    for key, value in d.items():
        cur_path = ".".join((path, key)) if len(path) else key
        if isinstance(value, int):
            print(cur_path, value)
        else:
            print_dict(value, cur_path)


print(print_dict_1(a))
