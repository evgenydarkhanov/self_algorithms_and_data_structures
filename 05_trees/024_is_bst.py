# является ли дерево бинарным деревом поиска

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_bst(root: TreeNode, left=float('-inf'), right=float('inf')) -> bool:
    if root is None:
        return True

    if not (left <= root.val <= right):
        return False

    return (
        is_bst(root.left, right=root.val)
        and is_bst(root.right, left=root.val)
    )


if __name__ == "__main__":
    n3 = TreeNode(3)
    n1 = TreeNode(1, left=n3)
    n2 = TreeNode(2)
    root = TreeNode(0, left=n1, right=n2)

    n_5 = TreeNode(5)
    n_3 = TreeNode(3)
    n_4 = TreeNode(4, left=n_3, right=n_5)
    n_1 = TreeNode(1)
    n_2 = TreeNode(2, left=n_1, right=n_4)

    assert not is_bst(root)
    assert is_bst(n_2)
