# найти зацикливание в связном списке

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Node) -> bool:
    """two pointers"""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return True

    return False


if __name__ == "__main__":
    lst1 = Node(1, next=Node(2, next=Node(3)))

    n3 = Node(3)
    n2 = Node(2, next=n3)
    n3.next = n2
    lst2 = Node(1, next=n2)

    assert not has_cycle(lst1)
    assert has_cycle(lst2)
