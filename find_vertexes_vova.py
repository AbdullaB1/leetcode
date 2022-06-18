from collections import defaultdict


class TreeNode:
    def __init__(self, left, right, value, id):
        self.left = left
        self.right = right
        self.value = value
        self.id = id


ALPHABET = 26


def get_num(c):
    return ord(c) - ord('A')


def dfs(node, founded):
    if not node:
        return 0
    node_founded = 1 << get_num(node.value)
    print(node.value)
    node_founded_set = node_founded | dfs(
        node.right, founded) | dfs(node.left, founded)
    print(node_founded_set)
    founded[node_founded_set].append(node)
    return node_founded_set


def get_equal_vertexes(root):
    founded = defaultdict(list)
    dfs(root, founded)
    result = []
    print(*map(lambda x: (x[0],
                          list(map(lambda x: (x.id, x.value), x[1]))
                          ), founded.items()), sep='\n')
    for value in founded.values():
        if len(value) > 1:
            result.append(list(map(lambda node: node.id, value)))
    return result


"""
     Z
    /   \
   C     B   # {CADB} {BADCD}
  / \   / \
  A  D  A  D
 /       \
B         C
           \
            D
"""

node1 = TreeNode(None, None, 'B', 1)
node2 = TreeNode(None, None, 'D', 2)
node4 = TreeNode(None, None, 'D', 4)
node5 = TreeNode(node1, None, 'A', 5)
node6 = TreeNode(node5, node2, 'C', 6)
node7 = TreeNode(None, node4, 'C', 7)
node3 = TreeNode(None, node7, 'A', 3)
node8 = TreeNode(None, None, 'D', 8)
node9 = TreeNode(node3, node8, 'B', 9)
root = TreeNode(node6, node9, 'Z', 10)

print(get_equal_vertexes(root))
