# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTMinIter:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.precess(root)

    def precess(self, root: Optional[TreeNode]):
        while root:
            self.stack.append(root)
            root = root.left

    def getNext(self):
        if self.stack:
            node = self.stack.pop()
            if node.right:
                self.precess(node.right)
            return node.val


class BSTMaxIter:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.precess(root)

    def precess(self, root: Optional[TreeNode]):
        while root:
            self.stack.append(root)
            root = root.right

    def getNext(self):
        if self.stack:
            node = self.stack.pop()
            if node.left:
                self.precess(node.left)
            return node.val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        min_iter = BSTMinIter(root)
        max_iter = BSTMaxIter(root)
        l = min_iter.getNext()
        r = max_iter.getNext()
        while l is not None and r is not None and l != r:
            curr = l + r
            if curr == k:
                return True
            if curr < k:
                l = min_iter.getNext()
            else:
                r = max_iter.getNext()
        return False
