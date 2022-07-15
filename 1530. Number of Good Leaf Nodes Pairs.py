class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 0
        self.dis = distance
        self.result = 0
        self.travers(root)
        return self.result
        
        
    def travers(self, node: TreeNode) -> list[int]:
        if not node.left and not node.right:
            return [1]
        depth, left, right = [], [], []
        if node.left:
            left = self.travers(node.left)
        if node.right:
            right = self.travers(node.right)
        # в этом месте было бы оптимальней использовать 2 отсортированных массива и идею из 2 sum in 2 array,
        # но проходит и без этого
        for l in left:
            for r in right:
                if r + l <= self.dis:
                    self.result += 1
        # а в этом merge 2 sorted arrays, но проходит и без этого
        for l in left:
            if l <= self.dis:
                depth.append(l + 1)
        for r in right:
            if r <= self.dis:
                depth.append(r + 1)
        return depth