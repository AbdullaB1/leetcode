# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        sum_el = 0

        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                sum_el += node.val
            if node.left and low < node.val:
                stack.append(node.left)
            if node.right and high > node.val:
                stack.append(node.right)

        return sum_el

        # q = deque([root])
        # sum = 0
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if low <= node.val <= high:
        #             sum += node.val
        #         if node.left and low < node.val:
        #             q.append(node.left)
        #         if node.right and high > node.val:
        #             q.append(node.right)
        # return sum
