import random
from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    max_key = max(arr)
    min_key = min(arr)
    offset = abs(min_key)
    size = max_key - min_key + 1

    out = [None for _ in range(n)]
    tmp = [0 for _ in range(size)]

    for elem in arr:
        tmp[elem + offset] += 1

    for i in range(1, size):
        tmp[i] += tmp[i - 1]

    for i in range(n - 1, -1, -1):
        idx = arr[i] + offset
        tmp[idx] -= 1
        out[tmp[idx]] = arr[i]

    return out
 

if __name__ == "__main__":
    arr = list(range(1_000))
    random.shuffle(arr)

    arrays = [
        arr,
        list(range(999, -1, -1)),
        [1, 0],
        [-1, 1, 0],
        [random.randint(-100, 100) for _ in range(1_000)],
    ]

    for arr in arrays:
        arr_reference = sorted(arr)
        arr_custom = counting_sort(arr)

        assert arr_custom == arr_reference, f'{arr_custom}'
