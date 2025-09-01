from typing import Optional, Sequence, TypeVar


T = TypeVar("T")


def binary_search(arr: Sequence[T], item: T) -> Optional[int]:
    """O(logn)"""
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if item == arr[mid]:
            return mid
        if item > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None


if __name__ == "__main__":
    arr = list(range(1_000_000))

    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 999_999) == 999_999
    assert binary_search(arr, 284_582) == 284_582
    assert binary_search(arr, 1_000_000) is None
    assert binary_search([], 42) is None
