def get_machines_count(machines: list[tuple[int, int]]):
    chages = []
    for m in machines:
        chages.append((m[0], 1))
        chages.append((m[0] + m[1], -1))
    chages.sort()
    print(chages)

    max_machines = 0
    cur_sum = 0
    begin = None
    prev_cur_sum = 0
    prev = None
    non_empty_intervals = []
    for time, val in chages:
        cur_sum += val

        if prev_cur_sum == 0 and prev != time:
            begin = time
            non_empty_intervals.append([begin, None])
        else:
            non_empty_intervals[-1][1] = time

        max_machines = max(max_machines, cur_sum)

        prev_cur_sum = cur_sum
    print(non_empty_intervals)
    return max_machines


machines: list[tuple[int, int]] = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    machines.append((l, r))
print(get_machines_count(machines))

# 6
# 13 4
# 15 1
# 11 5
# 12 3
# 10 3
# 30 3
