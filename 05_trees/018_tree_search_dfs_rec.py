# найти элемент в дереве или None

from typing import Any, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_dfs(root: TreeNode, k: Any) -> Optional[TreeNode]:
    """DFS, pre-order, recursion"""
    if not root:
        return None
    if root.val == k:
        return root
    else:
        return search_dfs(root.left, k) or search_dfs(root.right, k)


if __name__ == "__main__":
    n3 = TreeNode(3)
    n1 = TreeNode(1, left=n3)
    n2 = TreeNode(2)
    root = TreeNode(0, left=n1, right=n2)

    assert search_dfs(root, 0) is root, f'{search_dfs(root, 0) = }'
    assert search_dfs(root, 1) is n1, f'{search_dfs(root, 1) = }'
    assert search_dfs(root, 2) is n2, f'{search_dfs(root, 2) = }'
    assert search_dfs(root, 3) is n3, f'{search_dfs(root, 3) = }'
    assert search_dfs(root, 4) is None
    assert search_dfs(None, 0) is None
