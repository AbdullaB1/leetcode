def sorted_squares(arr):
    n = len(arr)
    if not n:
        return []
    left = 0  # заведем указатель на левую часть массива
    arr[0] *= arr[0]
    for idx in range(1, n):
        arr[idx] *= arr[idx]  # сразу возведем в квадрат
        while left >= 0 and arr[left] < arr[idx]:
            # если левый элемент меньше текущего, то выводим пока можем
            yield arr[left]
            left -= 1
        # это условие обрабатывет случай [3,2,1], т.к. нужно дойти до конца
        if left + 1 == idx:
            left += 1
        else:
            yield arr[idx]  # сюда попадаем, если есть разрыв между left и idx,
            # но перед этим все arr[left] < arr[idx] вывели, значит текущий уже наименьший
    # обрабатываем случай [3,2,1], т.е. когда весь массив убывает
    while left >= 0:
        yield arr[left]
        left -= 1


print(*sorted_squares(
    [-5, -3, -1, 0, 2, 4, 6]
))
