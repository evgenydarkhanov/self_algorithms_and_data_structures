from typing import TypeVar, Sequence, Optional


T = TypeVar("T")


def linear_search(arr: Sequence[T], item: T) -> Optional[int]:
    """O(n)"""
    for index, elem in enumerate(arr):
        if elem == item:
            return index
    return None


if __name__ == "__main__":
    arr = list(range(1_000_000))

    assert linear_search(arr, 0) == 0
    assert linear_search(arr, 999_999) == 999_999
    assert linear_search(arr, 284_582) == 284_582
    assert linear_search(arr, 1_000_000) is None
    assert linear_search([], 42) is None
