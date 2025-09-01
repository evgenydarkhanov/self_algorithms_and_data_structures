from typing import Any, Optional


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next = None


def linked_list_search(head: Node, item: Any) -> Optional[Node]:
    """O(n)"""
    while head is not None:
        if head.val == item:
            return head
        head = head.next

    return None


if __name__ == "__main__":
    head = Node(0)
    head_start = head

    for i in range(1, 5):
        node = Node(i)
        head.next = node
        head = node


    assert linked_list_search(head_start, 0).val == 0
    assert linked_list_search(head_start, 1).val == 1
    assert linked_list_search(head_start, 2).val == 2
    assert linked_list_search(head_start, 3).val == 3
    assert linked_list_search(head_start, 4).val == 4
    assert linked_list_search(head_start, 5) is None
    assert linked_list_search(None, 5) is None
