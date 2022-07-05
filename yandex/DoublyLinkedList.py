from typing import Optional


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next: Optional[Node]  = None
        self.prev: Optional[Node]  = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = Node()
        self.tail: Optional[Node] = Node()
        self.len = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return self.len

    def add_node(self, node: Node) -> None:
        self.len += 1
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node) -> None:
        self.len -= 1
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node: Node) -> None:
        self.remove_node(node)
        self.add_node(node)

    def pop_node(self) -> Node:
        for_del = self.tail.prev
        self.remove_node(for_del)
        return for_del

    def print_list(self) -> None:
        print("_______")
        curr = self.head.next
        while curr.next:
            print(curr.key, curr.val)
            curr = curr.next


ddl = DoublyLinkedList()
ddl.add_node(Node(1, 1))
ddl.add_node(Node(2, 2))
ddl.add_node(Node(3, 3))
ddl.add_node(Node(4, 4))
a = Node(5, 5)
ddl.add_node(a)
ddl.add_node(Node(6, 6))
ddl.add_node(Node(7, 7))
ddl.print_list()
ddl.pop_node()
ddl.print_list()
ddl.move_to_head(a)
ddl.print_list()
print(len(ddl))
{1:11}.popitem(last=False)