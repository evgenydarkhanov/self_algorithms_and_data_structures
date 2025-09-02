import random
from typing import Any, List


def merge_sort(arr: List[Any]) -> List[Any]:
    """
    Time:
        best: O(n log n)
        average: O(n log n)
        worst: O(n log n)
    Space:
        O(n)
    """
    n = len(arr)
    if n <= 1:
        return arr

    left = merge_sort(arr[:n//2])
    right = merge_sort(arr[n//2:])

    out = [None for _ in range(n)]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out[k] = left[i]
            i += 1
        else:
            out[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        out[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        out[k] = right[j]
        j += 1
        k += 1

    return out


def pythonic_merge_sort(arr: List[Any]) -> List[Any]:
    """питоничнее"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = pythonic_merge_sort(arr[:mid])
    right = pythonic_merge_sort(arr[mid:])

    out = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1

    out.extend(left[i:])
    out.extend(right[j:])

    return out


if __name__ == "__main__":
    arr = list(range(1_000))
    random.shuffle(arr)

    arrays = [
        arr,
        list(range(999, -1, -1)),
        [],
        [1, 0],
        [0, -1, 1],
        ['a', 'c', 'b'],
        ['aaa', 'aa', 'a']
    ]

    for arr in arrays:
        arr_reference = sorted(arr)
        arr_custom = merge_sort(arr)
        arr_pythonic = pythonic_merge_sort(arr)

        assert arr_custom == arr_reference == arr_pythonic, f'{arr_custom}\n{arr_pythonic}'
