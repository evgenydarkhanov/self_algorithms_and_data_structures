# обойти бинарное дерево in-order
#   0
#  1 2  -->  3 1 0 2
# 3

from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_in_order(root: TreeNode) -> Optional[List[Any]]:
    if not root:
        return None

    node = root
    stack = []
    result = []

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        result.append(node.val)
        node = node.right

    return result


if __name__ == "__main__":
    n3 = TreeNode(3)
    n1 = TreeNode(1, left=n3)
    n2 = TreeNode(2)
    root = TreeNode(0, left=n1, right=n2)

    assert traverse_in_order(root) == [3, 1, 0, 2]
