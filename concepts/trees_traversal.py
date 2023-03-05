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


def in_order(node):
    if node:
        in_order(node.left)
        print(node.val)
        in_order(node.right)


# in order print
in_order(root)
print("\n")


def pre_order(node):
    if node:
        print(node.val)
        pre_order(node.left)
        pre_order(node.right)


pre_order(root)
print("\n")


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.val)


post_order(root)

# So essentially
# - in order is left, root, right
# - pre order is root, left, right
# - post order is left, right , root
# Frankly, these are traversal methods only
