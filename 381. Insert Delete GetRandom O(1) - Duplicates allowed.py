import random
from collections import defaultdict


class RandomizedCollection_1:
    """
    решение через хранение в списке значения и его индекса в списке словаря
    в словаре просто храним список индексов этого значения в списке для выдачи рандомного элемента
    """
    def __init__(self):
        self._dict: dict[int, list[int]] = {}
        self._list: list[int] = []

    def insert(self, val: int) -> bool:
        # print("insert", val)
        # print(self._dict)
        # print(self._list)
        if val in self._dict:
            self._dict[val].append(len(self._list))
            self._list.append([val, len(self._dict[val]) - 1])
            return False
        
        self._dict[val] = [len(self._list)]
        self._list.append([val, 0])
        return True
        
    def remove(self, val: int) -> bool:
        # print("remove", val)
        # print(self._dict)
        # print(self._list)
        dict_val = self._dict.get(val, False)
        if not dict_val:
            return False
        index = self._dict[val][-1]
        self._list[index], self._list[-1] = self._list[-1], self._list[index]
        self._dict[self._list[index][0]][self._list[index][1]] = index
        self._dict[val].pop()
        self._list.pop()
        if self._dict[val] == []:
            self._dict.pop(val)
        return True
                                   
    def getRandom(self) -> int:
        return self._list[random.randrange(0, len(self._list))][0]
        


class RandomizedCollection:
    """
    более удобное решение
    в словаре храним set из индексов в списке
    список же содержит просто само значение
    """
    def __init__(self):
        self.dict = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        self.list.append(val)
        self.dict[val].add(len(self.list) - 1)
        return len(self.dict[val]) == 1
        
    def remove(self, val: int) -> bool:
        # print(f'{self.dict=} {self.list=}, {val=}')
        if val not in self.dict:
            return False
        # удалили в самом начале, потом удалять уже не нужно
        idx = self.dict[val].pop()
        if idx == len(self.list) - 1:
            self.list.pop()
            if not self.dict[val]:
                self.dict.pop(val)
            return True
        self.list[-1], self.list[idx] = self.list[idx], self.list[-1]
        self.dict[self.list[idx]].remove(len(self.list) - 1)
        self.dict[self.list[idx]].add(idx)
        # self.dict[val].remove(idx)
        self.list.pop()
        if not self.dict[val]:
            self.dict.pop(val)
        return True
                       
    def getRandom(self) -> int:
        return random.choice(self.list)

   
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
   