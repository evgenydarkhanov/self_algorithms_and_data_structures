from typing import Any, Optional


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next = None


def reverse_linked_list(head: Node) -> Optional[Node]:
    if head is None:
        return None

    node = head
    stack = []

    while node:
        stack.append(node)
        node = node.next

    head = stack.pop()
    current = head

    while stack:
        node = stack.pop()
        current.next = node
        current = node

    current.next = None

    return head


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
