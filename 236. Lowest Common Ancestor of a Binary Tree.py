from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # рекурсивный метод
    # в описании решения есть более хитрый способ рещения через стек за один проход по дереву
    def lowestCommonAncestor_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        self.travers(root, p, q)
        return self.lca

    def travers(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        left = right = mid = False
        if node.left:
            left = self.travers(node.left, p, q)
        if node.right:
            right = self.travers(node.right, p, q)
        if node.val == p.val or node.val == q.val:
            mid = True
        if mid + left + right >= 2:
            self.lca = node
        return mid or left or right

    # Работает сильно медленней

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.getNodePath(root, p.val)
        q_path = self.getNodePath(root, q.val)
        start_index = min(len(p_path), len(q_path))
        for i in range(start_index - 1, -1, -1):
            if p_path[i] == q_path[i]:
                return TreeNode(p_path[i])

    def getNodePath(self, root: 'TreeNode', target: int) -> List[int]:
        stack = [[root, [root.val]]]
        while stack:
            node, path = stack.pop()
            if node.val == target:
                return path
            if node.left:
                stack.append([node.left, path + [node.left.val]])
            if node.right:
                stack.append([node.right, path + [node.right.val]])
