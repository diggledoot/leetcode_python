class TNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


root = TNode(1)
root.left = TNode(2)
root.right = TNode(3)
root.left.left = TNode(4)
root.left.right = TNode(5)
root.right.left = TNode(6)
root.right.right = TNode(7)

root2 = TNode(1)
root2.left = TNode(2)
root2.right = TNode(3)
root2.left.left = TNode(4)
root2.left.right = TNode(5)
root2.right.left = TNode(6)
root2.right.right = TNode(7)


def compare(a: TNode, b: TNode):
    if a == None and b == None:
        return True

    if a == None or b == None:
        return False

    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)


print(compare(root, root2))
