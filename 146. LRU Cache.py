from collections import OrderedDict


# можно реализовтаь через OrderedDict
# При добавлении или запросе элемента, мы перемещаем его в конец,
# а удаляем из начала, тк элемента по умолчанию добавляются в конец
class LRUCacheWithOrderedDict:

    def __init__(self, capacity):
        self.orderedDict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.orderedDict:
            return -1
        self.orderedDict.move_to_end(key)
        return self.orderedDict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.orderedDict:
            self.orderedDict.move_to_end(key)
        self.orderedDict[key] = value
        if self.capacity < len(self.orderedDict):
            self.orderedDict.popitem(last=False)


class LRUCache:
    """решение, использующее то, что в питоне ключи хранятся в LIFO"""
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # таким способом можно удалить элемент из начала
            for key in self.cache:
                self.cache.pop(key)
                break


# реализация через двусвязный список и словарь
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def add_node(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node: Node) -> None:
        self.remove_node(node)
        self.add_node(node)

    def pop_node(self) -> Node:
        for_del = self.tail.prev
        self.remove_node(for_del)
        return for_del

    def __init__(self, capacity):
        self.head = Node()
        self.tail = Node()
        self.cache = {}
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
            return
        node = Node(key, value)
        self.add_node(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            self.cache.pop(self.pop_node().key)

    def print_list(self) -> None:
        print("----------------")
        print(*map(lambda x: (x[0], (x[1].key, x[1].val)),
              self.cache.items()), sep="\n")
        curr = self.head.next
        while curr.next:
            print(curr.key, curr.val)
            curr = curr.next


# ddl = LRUCache()
# ddl.add_node(Node(1, 1))
# ddl.add_node(Node(2, 2))
# ddl.add_node(Node(3, 3))
# ddl.add_node(Node(4, 4))
# a = Node(5, 5)
# ddl.add_node(a)
# ddl.add_node(Node(6, 6))
# ddl.add_node(Node(7, 7))
# ddl.print_list()
# ddl.pop_node()
# ddl.print_list()
# ddl.move_to_head(a)
# ddl.print_list()

lru = LRUCache(3)
lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3)
lru.put(4, 4)
lru.put(5, 5)
lru.get(3)
lru.put(6, 6)
lru.put(7, 7)
lru.print_list()
