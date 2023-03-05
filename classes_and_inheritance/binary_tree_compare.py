class TNode:
    def __init__(self, value=0) -> None:
        self.value = value
        self.left = None
        self.right = None


root1 = TNode(1)
root1.left = TNode(2)
root1.right = TNode(3)

root2 = TNode(1)
root2.left = TNode(2)
root2.right = TNode(3)

print(root1, root2)


def compare(a: TNode, b: TNode):
    if a == None and b == None:
        return True

    if a == None or b == None:
        return False

    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)


print(compare(root1, root2))
