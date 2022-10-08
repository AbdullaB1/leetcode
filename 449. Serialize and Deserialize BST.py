import json
from typing import Optional
import math
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# решение в лоб через json
class Codec_2:
    def serialize(self, root: Optional[TreeNode]) -> str:
        return json.dumps(self.ser_rec(root))
    
    def ser_rec(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '{}'
        
        return {
            'root': root.val, 
            'left': self.ser_rec(root.left),
            'right': self.ser_rec(root.right),
        }
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dec_data = json.loads(data)
        return self.des_rec(dec_data)
          
    def des_rec(self, node: dict) -> Optional[TreeNode]:
        if not 'root' in node:
            return None
        result =  TreeNode(int(node['root']))
        result.left = self.des_rec(node['left']) 
        result.right = self.des_rec(node['right'])
        return result


# решение с использованием минимального количества символов
# (только значения вершин и символ разделителя)
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        res = []
        stack = []
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            node = node.right
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
        return ' '.join(map(str, res))
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        q = deque(map(int, data.split()))
        return self.travers(q, -math.inf, math.inf)
         
    def travers(self, q: deque[int], min_val: int, max_val: int) -> Optional[TreeNode]:
        if not q:
            return None
        
        if q and q[0] > max_val:
            return None
        val = q.popleft()
        node = TreeNode(val)
        node.left = self.travers(q, min_val, val)
        node.right = self.travers(q, val, max_val)
        return node


codec = Codec()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print(serialized := codec.serialize(root))
print(deserialized := codec.deserialize(serialized))
assert codec.serialize(root) == codec.serialize(deserialized)
