# инвертировать бинарное дерево
#   0         0
#  1 2  -->  2 1
# 3             3

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> None:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)


if __name__ == "__main__":
    n3 = TreeNode(3)
    n1 = TreeNode(1, left=n3)
    n2 = TreeNode(2)
    root = TreeNode(0, left=n1, right=n2)

    invert_tree(root)
    assert root.left is n2
    assert root.right is n1
    assert root.right.right is n3
