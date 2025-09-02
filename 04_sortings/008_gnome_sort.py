import random
from typing import Any, List


def gnome_sort(arr: List[Any]) -> None:
    """
    Time:
        best: O(n)
        average: O(n^2)
        worst: O(n^2)
    Space:
        O(1)
        in place
    """
    i = 1
    n = len(arr)
    while i < n:
        if arr[i] >= arr[i-1]:
            i += 1
            continue
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
            if i < 1:
                i += 1


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
        gnome_sort(arr)

        assert arr == arr_sorted, f'{arr}'
