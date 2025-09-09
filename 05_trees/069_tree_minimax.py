"""
Дано бинарное дерево поиска в виде массива.
Необходимо найти произведение минимального и максимального значений.
Для этого необходимо вспомнить как бинарное дерево размещается в массиве

root = 0
parent = (i - 1)/2
left = 2i + 1
right = 2i + 2
"""

from typing import List


def tree_min_max(tree: List[int]) -> int:
    n = len(tree)
    if n == 2:
        return tree[0] * tree[1]

    l, r = 0, 0

    while l < n:
        l = 2 * l + 1
    l = (l - 1) // 2

    while r < n:
        r = 2 * r + 2
    r = (r - 1) // 2

    return tree[l] * tree[r]


if __name__ == "__main__":
    assert tree_min_max([16, 11, 18, 9, 13, 17, 21, 7, 10, 12, 15]) == 147, tree_min_max([16, 11, 18, 9, 13, 17, 21, 7, 10, 12, 15])
