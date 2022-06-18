def get_machines_count(machines: list[tuple[int, int]]):
    chages = []
    for m in machines:
        chages.append((m[0], 1))
        chages.append((m[0] + m[1], -1))
    chages.sort()
    max_machines = 0
    cur_sum = 0
    for _, val in chages:
        cur_sum += val
        max_machines = max(max_machines, cur_sum)
    return max_machines


machines: list[tuple[int, int]] = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    machines.append((l, r))
print(get_machines_count(machines))

# input
# 5
# 13 4
# 15 1
# 11 5
# 12 3
# 10 3
