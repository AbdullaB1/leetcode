# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    # Задача 3 https://youtu.be/j6_lW7W5AZs
    # O(h1 - h2) - зависит от перепада высот между нодами
    # мы за 2 * (h1 - h2) гарантированно найдем перепад высот,
    # затем уже зная перепад, подтянем более низкую ноду до высоты верхней,
    # затем будем подниматься вверх по каждой, до первого совпадения
    def getDiff(self, p: 'Node', q: 'Node', pow2: int) -> 'Node':
        first = p
        second = q
        steps = 0
        for i in range(2**pow2):
            if first.parent:
                first = first.parent
                steps += 1
        for i in range(2**pow2):
            if second == first:
                return steps - i
            if second.parent:
                second = second.parent
            else:
                break
        return -1

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pow2 = 0
        res = None
        while True:
            res = self.getDiff(p, q, pow2)
            if res >= 0:
                break
            res = self.getDiff(q, p, pow2)
            if res >= 0:
                p, q = q, p
                break
            pow2 += 1

        while res > 0:
            p = p.parent
            res -= 1
        while p != q:
            p = p.parent
            q = q.parent
        return p

    # Более элегантное решение
    # Идем наверх до корня, когда дошли до корня, начинаем идти с начала, поменяв для кадой ноды старт
    # В итоге получается, что каждым указателем мы пробегаем одинаковое растояние,
    # и на финише значения начнут совпадать, первое же совпадения будет являться LCA
    def lowestCommonAncestor_1(self, p: Node, q: Node) -> Node:
        first = p
        second = q
        while first != second:
            if first.parent:
                first = first.parent
            else:
                first = q
            if second.parent:
                second = second.parent
            else:
                second = p
        return first

    # считаем расстояние до корня от каждой ноды,
    # затем выравниваем расстояния до корня у каждой ноды,
    # когда они сравняются, начинаем на каждом шагу идти вверх,
    # пока они не совпадут
    # Первое совпадение будет являться LCA
    def lowestCommonAncestor_2(self, p: Node, q: Node) -> Node:
        p_path = 0
        curr = p
        while curr.parent:
            p_path += 1
            curr = curr.parent
        q_path = 0
        curr = q
        while curr.parent:
            q_path += 1
            curr = curr.parent
        if p_path < q_path:
            p, q = q, p
            p_path, q_path = q_path, p_path
        while p_path > q_path:
            print(p.val)
            p = p.parent
            p_path -= 1
        while p != q:
            p = p.parent
            q = q.parent
        return p
