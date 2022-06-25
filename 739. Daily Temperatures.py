from typing import List


class Solution:
    # такой тест ничего не портит, так как для 100 мы определим день за О(1)
    #[101, 1, 2, 3, 4, 5, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n

        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                # если это самая высокая тмпература,
                # то нет смысла смотреть дальше, теплей не будет
                continue

            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # если предидущий день не теплей, то посмотрим,
                # какой день был теплей предидущего,
                # и так пока не найдем результат
                # ответ точно есть, так как иначе мы бы определили это шагом ранее
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer


class Solution_1:
    # через стеек, итерируемся с начала массива
    # преимущество в том, что можно обрабатывать данные в потоке
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        result = [0] * len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result


class Solution_2:
    # итетируемся с конца массива
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        result = [0] * len(temps)
        stack = []
        for i in range(len(temps) - 1, -1, -1):
            # важное отличие в том, что если в стеке значени совпадают, 
            # то старое нужно удалить, потому что появилось более свежее, 
            # дающее нам в препективе меньшую разницу
            while stack and temps[stack[-1]] <= temps[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result


s = Solution()
print(
    s.dailyTemperatures(
        # [73, 74, 77, 71, 69, 72, 76, 73]
        [100, 1, 2, 3, 4, 5, 101, 1, 2, 3, 4, 5, 6, 7, 8, 102]
    )
)
