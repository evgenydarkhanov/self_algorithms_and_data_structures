import random
from typing import List


def counting_sort(arr: List[int], key) -> List[int]:
    if not arr:
        return arr

    n = len(arr)
    m = max(key(elem) for elem in arr)

    out = [None for _ in range(n)]
    tmp = [0 for _ in range(m + 1)]

    for elem in arr:
        tmp[key(elem)] += 1

    for i in range(1, m + 1):
        tmp[i] += tmp[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        elem = arr[i]
        index = key(arr[i])
        out[tmp[index] - 1] = elem
        tmp[index] -= 1

    return out


def radix_sort(arr: List[int]) -> List[int]:
    if not arr:
        return arr

    k = max(arr)
    digit = 1

    while digit <= k:
        arr = counting_sort(arr, key=lambda x: (x // digit) % 10)
        digit *= 10

    return arr


if __name__ == "__main__":
    arr = list(range(1_000))
    random.shuffle(arr)

    arrays = [
        arr,
        list(range(999, -1, -1)),
        [1, 0],
        [0, 0, 0, 0],
        [],
        [1, 2, 3, 4],
    ]

    for arr in arrays:
        arr_reference = sorted(arr)
        arr_custom = radix_sort(arr)

        assert arr_custom == arr_reference, f'{arr_custom}'
