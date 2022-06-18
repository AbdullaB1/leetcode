# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
