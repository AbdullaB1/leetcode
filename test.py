def painted(inters: list[tuple[int, int]]) -> int:
    result = 0
    events = []
    for inter in inters:
        events.append((inter[0], 1))
        events.append((inter[1], -1))
    events.sort()
    cursum = 0
    prev = 0
    for e in events:
        if e[1] == -1:
            cursum -= 1
            if cursum == 0:
                result += e[0] - prev
                prev = e[0]
        else:
            cursum += 1
            if cursum == 1:
                prev = e[0]
    if cursum > 0:
        result += events[-1][0] - prev
    return result


print(
    painted([(1, 5), (3, 6)])
)
print(
    painted([(1, 2), (3, 6)])
)
print(
    painted([(1, 5), (3, 6), (4, 7), (20, 21)])
)
print(
    painted([(1, 5), (9, 15)])
)
