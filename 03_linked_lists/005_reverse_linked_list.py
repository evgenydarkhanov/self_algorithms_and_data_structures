from typing import Any, Optional


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next = None


def reverse_linked_list(head: Node) -> Optional[Node]:
    """O(n)"""
    if head is None:
        return None
    node = head
    prev = None
    while node:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node

    return prev


if __name__ == "__main__":
    head = Node(0)
    head_start = head
    for i in range(1, 5):
        node = Node(i)
        head.next = node
        head = node

    reversed_head = reverse_linked_list(head_start)
    assert reversed_head.val == 4
    assert reversed_head.next.val == 3
