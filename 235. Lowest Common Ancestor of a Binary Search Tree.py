class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node


        # плохое решение не использующее свойство бинарного дерева поиска
        # находим путь до корня для каждой ноды, потом через странение ищем LCA 
#         def findWithPath(root: Optional[TreeNode], target: int) -> List[int]:
#             if not root:
#                 return []
#             if root.val == target:
#                 return [target]
#             if root.val > target:
#                 result = findWithPath(root.left, target)
#             else:
#                 result = findWithPath(root.right, target)
#             if result:
#                 result.append(root.val)
#             return result
        
#         p_path = findWithPath(root, p.val)
#         q_path = findWithPath(root, q.val)
#         # print(p_path)
#         # print(q_path)
#         last = 0
#         for i in range(-1, -min(len(p_path), len(q_path)) - 1, -1):
#             if p_path[i] == q_path[i]:
#                 last = p_path[i]
#             else:
#                 break
#         return TreeNode(last)
