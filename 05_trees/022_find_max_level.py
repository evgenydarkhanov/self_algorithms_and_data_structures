# вернуть список максимальных элементов с каждого уровня бинарного дерева
#   0
#  1 2  -->  [0, 2, 3]
# 3

from collections import deque
from typing import Any, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_max_level(root: TreeNode) -> List[Any]:
    if not root:
        return None

    queue = deque([(0, root)])
    result = []

    while queue:
        level, node = queue.popleft()

        if len(result) <= level:
            result.append(node.val)
        elif node.val > result[level]:
            result[level] = node.val

        if node.left:
            queue.append((level + 1, node.left))
        if node.right:
            queue.append((level + 1, node.right))

    return result


if __name__ == "__main__":
    n3 = TreeNode(3)
    n1 = TreeNode(1, left=n3)
    n2 = TreeNode(2)
    root = TreeNode(0, left=n1, right=n2)

    assert search_max_level(root) == [0, 2, 3], f'{search_max_level(root)} = '
