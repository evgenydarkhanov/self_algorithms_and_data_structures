import random
from typing import Any, List


def partition(arr: List[Any], left: int, right: int) -> int:
    x = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr: List[Any], left: int, right: int):
    """
    Time:
        best: O(n log n)
        average: O(n log n)
        worst: O(n^2)
    Space:
        O(1), in place
    """
    if left < right:
        q = partition(arr, left, right)
        quick_sort(arr, left, q - 1)
        quick_sort(arr, q + 1, right)


if __name__ == "__main__":
    arr = list(range(100))
    random.shuffle(arr)

    arrays = [
        arr,
        list(range(99, -1, -1)),
        [],
        [1, 0],
        [0, -1, 1],
        ['a', 'c', 'b'],
        ['aaa', 'aa', 'a']
    ]

    for arr in arrays:
        arr_reference = sorted(arr)
        quick_sort(arr, 0, len(arr) - 1)

        assert arr == arr_reference, f'{arr}'
