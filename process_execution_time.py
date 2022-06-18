from collections import defaultdict


# проверка графа на циклы
# https://e-maxx.ru/algo/finding_cycle
# топологическая сортировка
# https://e-maxx.ru/algo/topological_sort


def dfs(v, graph, runtimes, color, visit_order):
    color[v] = 1  # visited before visit children
    acc = 0
    for to in graph[v]:
        if color[to] == 0:  # not visited
            if dfs(to, graph, runtimes, color, visit_order):
                return True
        elif color[to] == 1:  # find cycle
            return True
        acc = max(acc, runtimes[to])
    color[v] = 2  # visited before after children
    runtimes[v] += acc
    visit_order.append(v)
    return False


def make_schedule(tasks: list[tuple[int, int, list[int]]]) -> tuple[list, int]:
    n = len(tasks)
    graph = defaultdict(list)
    runtimes = [0] * n
    for task, runtime, subtasks in tasks:
        runtimes[task] = runtime
        graph[task] = subtasks

    visit_order = []
    color = [0] * n
    for v in range(n):
        if color[v] == 0 and dfs(v, graph, runtimes, color, visit_order):
            return None

    return visit_order, max(runtimes)


sample1 = [
    (0, 1, [1]),
    (2, 1, [1]),
    (3, 3, [1, 5]),
    (1, 1, [4]),
    (4, 1, []),
    (5, 1, [4]),
]

print(make_schedule(sample1))
