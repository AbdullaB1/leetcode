from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    рекурсивный метод
    в описании решения есть более хитрый способ решения через стек за один проход по дереву без рекурсии
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        self.traverse(root, p, q)
        return self.lca
    
    
    def traverse(self, node: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        left, right, mid = False, False, False
        if node.left:
            left = self.traverse(node.left, p, q)
        if node.right:
            right = self.traverse(node.right, p, q)
        mid = node.val == p.val or node.val == q.val
        if left + right + mid >= 2:
            self.lca = node
        return left or right or mid
        

class Solution_1: 
    """
    работает сильно медленней, находим путь до корня для p и q, затем ищем первое совпадение в путях
    """  
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
     