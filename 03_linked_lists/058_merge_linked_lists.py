from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional

"""
Дан массив k связных списков, каждый связный список отсортирован в порядке возрастания.

Смёрджите все связные списки в один связный список и верните его.

Пример 1:
Ввод: lists = [[1,4,5],[1,3,4],[2,6]]
Вывод: [1,1,2,3,4,4,5,6]
"""

@dataclass
class Node:
    val: Any
    next: Optional[Node] = None


def merge_two_lists(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
    if not head1:
        return head2
    if not head2:
        return head1

    # фиктивная голова
    dummy = Node(val=0)
    curr = dummy

    while head1 and head2:
        if head1.val <= head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next

        curr = curr.next

    curr.next = head1 or head2

    return curr.next


def merge_linked_lists(lists: List[Node]) -> Optional[Node]:
    n = len(lists)
    if n == 0:
        return None

    if n == 1:
        return lists[0]

    head = merge_two_lists(lists[0], lists[1])
    if n == 2:
        return head

    for i in range(2, n):
        tmp = merge_two_lists(head, lists[i])
        head = tmp

    return head
