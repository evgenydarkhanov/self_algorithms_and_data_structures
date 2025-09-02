import random
from typing import Any, List


MIN_MERGE = 32

def calc_minrun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(arr: List[Any]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_subarrays(arr: List[Any]) -> List[Any]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_subarrays(arr[:mid])
    right = merge_subarrays(arr[mid:])

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


def almost_timsort(arr: List[Any]) -> List[Any]:
    """
    Time:
        best: O(n)
        average: O(n log n)
        worst: O(n log n)
    Space:
        O(n)
    """
    n = len(arr)
    if n < MIN_MERGE:
        insertion_sort(arr)
        return arr

    minrun = calc_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun, n)
        insertion_sort(arr[start:end])

    out = merge_subarrays(arr)
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
        arr_custom = almost_timsort(arr)

        assert arr_custom == arr_reference, f'{arr_custom}'
