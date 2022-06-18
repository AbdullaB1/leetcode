from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # попробовать реализовать итеративно
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass

    # рекуксивный метод
    def maxPathSum_1(self, root: Optional[TreeNode]) -> int:
        self.max_path = -math.inf
        self.travers(root)
        return self.max_path

    def travers(self, node: Optional[TreeNode]) -> int:
        left = right = -math.inf
        if node.left:
            left = self.travers(node.left)
        if node.right:
            right = self.travers(node.right)
        self.max_path = max(
            self.max_path,
            left + right + node.val,
            left + node.val,
            right + node.val,
            node.val,
            left,
            right
        )
        return max(left + node.val, right + node.val, node.val)
