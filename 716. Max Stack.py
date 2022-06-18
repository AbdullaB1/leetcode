class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.max_stack.append(x)
            return
        self.stack.append(x)
        self.max_stack.append(max(self.max_stack[-1], x))

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_elem = self.max_stack[-1]
        temp = []
        while self.stack[-1] != max_elem:
            temp.append(self.stack.pop())
            self.max_stack.pop()
        self.stack.pop()
        self.max_stack.pop()
        while temp:
            self.push(temp.pop())
        return max_elem

# https://leetcode.com/problems/max-stack/solution/ (премиум)
# есть еще решение на джава
# значения храним в связном списке, чтобы легко можно было удалять макисамльный элемент из середины
# В TreeMap храним ссылки на ноды, чтобы по ним легко удалять элементы из связного списка
# Получаения максимума занимает log n, так как для этого мы просто смотрим на самый правй лист в дереве - map.lastKey()
# class MaxStack {
#     TreeMap<Integer, List<Node>> map;
#     DoubleLinkedList dll;

#     public MaxStack() {
#         map = new TreeMap();
#         dll = new DoubleLinkedList();
#     }

#     public void push(int x) {
#         Node node = dll.add(x);
#         if(!map.containsKey(x))
#             map.put(x, new ArrayList<Node>());
#         map.get(x).add(node);
#     }

#     public int pop() {
#         int val = dll.pop();
#         List<Node> L = map.get(val);
#         L.remove(L.size() - 1);
#         if (L.isEmpty()) map.remove(val);
#         return val;
#     }

#     public int top() {
#         return dll.peek();
#     }

#     public int peekMax() {
#         return map.lastKey();
#     }

#     public int popMax() {
#         int max = peekMax();
#         List<Node> L = map.get(max);
#         Node node = L.remove(L.size() - 1);
#         dll.unlink(node);
#         if (L.isEmpty()) map.remove(max);
#         return max;
#     }
# }

# class DoubleLinkedList {
#     Node head, tail;

#     public DoubleLinkedList() {
#         head = new Node(0);
#         tail = new Node(0);
#         head.next = tail;
#         tail.prev = head;
#     }

#     public Node add(int val) {
#         Node x = new Node(val);
#         x.next = tail;
#         x.prev = tail.prev;
#         tail.prev = tail.prev.next = x;
#         return x;
#     }

#     public int pop() {
#         return unlink(tail.prev).val;
#     }

#     public int peek() {
#         return tail.prev.val;
#     }

#     public Node unlink(Node node) {
#         node.prev.next = node.next;
#         node.next.prev = node.prev;
#         return node;
#     }
# }

# class Node {
#     int val;
#     Node prev, next;
#     public Node(int v) {val = v;}
# }
