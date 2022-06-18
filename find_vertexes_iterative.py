from collections import defaultdict


class TreeNode:
    def __init__(self, left, right, value, id):
        self.left = left
        self.right = right
        self.value = value
        self.id = id


def travers(root: TreeNode, founded: defaultdict[int, list]) -> int:
    node_value = 1 << (ord(root.value) - ord('A'))
    if root.left:
        node_value |= travers(root.left, founded)
    if root.right:
        node_value |= travers(root.right, founded)
    founded[node_value].append(root)
    return node_value


def get_equal_vertexes(root: TreeNode) -> list[str]:
    if not root:
        return []
    founded = defaultdict(list)
    travers(root, founded)
    result = []
    for key, value in founded.items():
        if len(value) > 1:
            result.append(
                list(map(lambda x: (x.value, x.id), value))
            )
    return result


def get_equal_vertexes_iterative(root: TreeNode) -> list[str]:
    if not root:
        return []
    founded = defaultdict(list)
    prev_ans = []
    stack = [(root, False)]
    while stack:
        node, is_for_insert = stack.pop()
        if is_for_insert:
            node_value = 1 << (ord(node.value) - ord('A'))
            children_count = bool(node.left) + bool(node.right)
            for _ in range(children_count):
                node_value |= prev_ans.pop()
            prev_ans.append(node_value)
            founded[node_value].append(node)
            continue
        stack.append((node, True))
        if node.left:
            stack.append((node.left, False))
        if node.right:
            stack.append((node.right, False))

    result = []
    for value in founded.values():
        if len(value) > 1:
            result.append(
                list(map(lambda x: (x.value, x.id), value))
            )
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
