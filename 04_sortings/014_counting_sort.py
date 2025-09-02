import random
from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """
    Time:
        O(n + k)
    Space:
        O(n + k)
    """
    n = len(arr)
    m = max(arr)

    out = [None for _ in range(n)]
    tmp = [0 for _ in range(m + 1)]

    for elem in arr:
        tmp[elem] += 1

    for i in range(1, m + 1):
        tmp[i] += tmp[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        elem = arr[i]
        index = tmp[elem] - 1
        out[index] = elem
        tmp[elem] -= 1

    return out
 

if __name__ == "__main__":
    arr = list(range(1_000))
    random.shuffle(arr)

    arrays = [
        arr,
        list(range(999, -1, -1)),
        [1, 0],
    ]

    for arr in arrays:
        arr_reference = sorted(arr)
        arr_custom = counting_sort(arr)

        assert arr_custom == arr_reference, f'{arr_custom}'
