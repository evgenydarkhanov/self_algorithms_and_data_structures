# найти элемент в дереве или None

from collections import deque
from typing import Any, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bfs(root: TreeNode, k: Any) -> Optional[TreeNode]:
    """BFS"""
    if not root:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.val == k:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return None


if __name__ == "__main__":
    n3 = TreeNode(3)
    n1 = TreeNode(1, left=n3)
    n2 = TreeNode(2)
    root = TreeNode(0, left=n1, right=n2)

    assert search_bfs(root, 0) is root, f'{search_bfs(root, 0) = }'
    assert search_bfs(root, 1) is n1, f'{search_bfs(root, 1) = }'
    assert search_bfs(root, 2) is n2, f'{search_bfs(root, 2) = }'
    assert search_bfs(root, 3) is n3, f'{search_bfs(root, 3) = }'
    assert search_bfs(root, 4) is None
    assert search_bfs(None, 0) is None
