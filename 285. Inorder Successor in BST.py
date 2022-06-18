# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> Optional[TreeNode]:
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

    # подходит для лбюбого дерева и не учитывает то, что это BST

    def inorderSuccessor_1(self, root: 'TreeNode', p: 'TreeNode') -> Optional[TreeNode]:
        stack = []
        while root:
            stack.append(root)
            root = root.left

        prev_p = False
        while stack:
            node = stack.pop()
            if prev_p:
                return node
            if node.val == p.val:
                prev_p = True
            node = node.right
            while node:
                stack.append(node)
                node = node.left
