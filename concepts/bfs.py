from collections import deque


class TNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


# Create the root node
root = TNode(1)

# Create the left subtree
root.left = TNode(2)
root.left.left = TNode(4)
root.left.right = TNode(5)

# Create the right subtree
root.right = TNode(3)
root.right.left = TNode(6)
root.right.right = TNode(7)


# also pre-order
def bfs(node, target):
    queue = deque([node])  # expect iterable

    while queue:
        node = queue.popleft()
        if node.val == target:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


print(bfs(root, 6).val)
