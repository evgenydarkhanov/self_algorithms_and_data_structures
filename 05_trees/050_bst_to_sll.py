from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional

# написать функцию, которая превращает Binary Search Tree в Single Linked List
# односвязный список должен содержать элементы дерева по возрастанию
# можно сделать DFS in-order


@dataclass(order=True)
class TreeNode:
    val: Any
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


@dataclass(order=True)
class ListNode:
    val: Any
    next: Optional[Node] = None


def bst_to_sll(root: Optional[TreeNode]) -> Optional[Node]:
    if not root:
        return None

    node = root
    stack = []
    list_node = None
    head = None

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()

        #
        if not list_node:
            list_node = ListNode(node.val)
            head = list_node
        else:
            list_node.next = ListNode(node.val)
            list_node = list_node.next

        node = node.right

    return head


if __name__ == "__main__":
    n_5 = TreeNode(5)
    n_3 = TreeNode(3)
    n_4 = TreeNode(4, left=n_3, right=n_5)
    n_1 = TreeNode(1)
    n_2 = TreeNode(2, left=n_1, right=n_4)

    assert bst_to_sll(n_2).val == 1, f"{bst_to_sll(n_2).val = }"
