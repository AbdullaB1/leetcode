# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


# предпочтительное решение, так как список может быть чень большим,
# и так поддерживаются ленивые вычисления
class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = [*nestedList][::-1]

    def addIntegetToTopOfStack(self) -> None:
        while self.stack and not self.stack[-1].isInteger():
            elem = self.stack.pop()
            if elem.isInteger():
                self.stack.append(elem.getInteger())
            else:
                elemList = elem.getList()
                for i in range(len(elemList) - 1, -1, -1):
                    self.stack.append(elemList[i])

    def next(self) -> int:
        self.addIntegetToTopOfStack()
        return self.stack.pop()

    def hasNext(self) -> bool:
        self.addIntegetToTopOfStack()
        return len(self.stack) > 0


# засунуть все сразу
# костыль против [[]] и подобных этому тестов, так как hasNext() тогда работает некорректно
class NestedIterator_1:
    def __init__(self, nestedList: List[NestedInteger]):
        stack = [*nestedList]
        self.result = []
        while stack:
            elem = stack.pop()
            if elem.isInteger():
                self.result.append(elem.getInteger())
            else:
                elemList = elem.getList()
                for i in range(len(elemList)):
                    stack.append(elemList[i])

    def next(self) -> int:
        return self.result.pop()

    def hasNext(self) -> bool:
        return len(self.result) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
