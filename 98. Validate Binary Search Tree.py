from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # итеративное решение
    # для каждого поддераева проверяем, что все значения находятся с правильных интервалах
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, min_val, max_val = stack.pop()
            if node.val <= min_val or node.val >= max_val:
                return False
            if node.left:
                stack.append((node.left, min_val, node.val))
            if node.right:
                stack.append((node.right, node.val, max_val))
        return True

    # итеративное решение
    # обходим дерево в порядке возрастания,
    # если все элементы больше предидущего, значит дерево валидное

    def isValidBST_3(self, root: Optional[TreeNode]) -> bool:
        prev = -math.inf

        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return True

    # рекусривно проходимся по дереву в порядке возрастания,
    # и проверяем, что каждый следующий элемент юольше предидущего

    def isValidBST_2(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf
        return self.inorder_travers(root)

    def inorder_travers(self, node: Optional[TreeNode]) -> bool:
        left = True
        if node.left:
            left = self.inorder_travers(node.left)
        if not left:
            return False
        if self.prev >= node.val:
            return False
        self.prev = node.val
        if node.right:
            return self.inorder_travers(node.right)
        return True

    # рекурсивно проверяем, что все значения в дереве лежат между maxVal и minVal

    def isValidBST_1(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)

    def validate(self, node: Optional[TreeNode], minVal, maxVal) -> bool:
        if node.val <= minVal or node.val >= maxVal:
            return False

        left, right = True, True
        if node.left:
            left = self.validate(node.left, minVal, node.val)
        if node.right:
            right = self.validate(node.right, node.val, maxVal)

        return left and right
