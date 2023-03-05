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


def dfs(node, target):
    if node is None:
        return None

    if node.val == target:
        return node

    left = dfs(node.left, target)
    if left:
        return left

    return dfs(node.right, target)


# the traversal method is pre order
print(dfs(root, 7).val)  # bad way of writing but i'm lazy atm
