from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self.get_min_max(root)
        return is_balanced

    def get_min_max(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return True, 0

        left_balanced, left_max = self.get_min_max(root.left)
        right_balanced, right_max = self.get_min_max(root.right)

        return left_balanced and right_balanced and abs(left_max - right_max) < 2, max(left_max, right_max) + 1
