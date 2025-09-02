import random
from typing import Any, List


def insertion_sort(arr: List[Any]) -> None:
    """
    Time:
        best: O(n)
        average: O(n^2)
        worst: O(n^2)
    Space:
        O(1)
        in place
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


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
        arr_sorted = sorted(arr)
        insertion_sort(arr)

        assert arr == arr_sorted, f'{arr}'
