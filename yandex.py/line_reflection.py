def line_reflection(points: list[list]) -> bool:
    if not points:
        return True
    points_set = set()
    minx = points[0][0]
    maxx = points[0][0]
    for p in points:
        points_set.add((p[0], p[1]))
        minx = min(minx, p[0])
        maxx = max(maxx, p[0])

    minmaxsum = minx + maxx

    for p in points:
        if (minmaxsum - p[0], p[1]) not in points_set:
            return False

    return True


print(
    line_reflection(
        [[-5, 0], [5, 0], [3, 4], [-3, 4], [-3, 4], [1, 1]]
    )
)
