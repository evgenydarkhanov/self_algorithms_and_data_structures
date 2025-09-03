# удалить из списка ноду с переданным значением
# что-то не так в последнем тесте, словно value одни, а id разные

from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: Optional[Node] = None


def remove_node(head: Node, k: int) -> Optional[Node]:
    if not head:
        return None

    if head.val == k:
        return head.next
    
    root = head
    node = head

    while node.next:
        prev = node
        node = node.next
        if node.val == k:
            prev.node = node.next
            return root

    return None


if __name__ == "__main__":
    n3 = Node(3)
    n2 = Node(2, next=n3)
    n1 = Node(1, next=n2)
    root = Node(0, next=n1)

    assert remove_node(root, 3) is root
    assert remove_node(root, 1) is root
    assert remove_node(root, 0) is n2, f'{n2.val = }'
