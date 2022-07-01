from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """рекурсивное отражение дерева и проверка равенства 2 деревьев через обход в ширину"""

    def reverseTree(self, head: Optional[TreeNode]):
        if not head:
            return head
        head.left, head.right = head.right, head.left
        self.reverseTree(head.left)
        self.reverseTree(head.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.reverseTree(root.left)

        q = deque([(root.left, root.right)])
        while q:
            for _ in range(len(q)):
                left, right = q.popleft()

                if not left and not right:
                    continue
                if not left:
                    return False
                if not right:
                    return False
                if left.val != right.val:
                    return False

                q.append((left.left, right.left))
                q.append((left.right, right.right))

        return True


class Solution_1:
    """полностью рукурсивное решение"""

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.revers(root.right)
        return self.is_tree_equals(root.left, root.right)

    def is_tree_equals(self, node_1: Optional[TreeNode], node_2: Optional[TreeNode]) -> bool:
        if not node_1 and not node_2:
            return True
        if not node_1:
            return False
        if not node_2:
            return False
        if node_1.val != node_2.val:
            return False
        if not self.is_tree_equals(node_1.left, node_2.left):
            return False
        if not self.is_tree_equals(node_1.right, node_2.right):
            return False
        return True

    def revers(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return node

        node.left, node.right = node.right, node.left
        self.revers(node.left)
        self.revers(node.right)
