import random
from typing import Any, List


def bubble_sort(arr: List[Any]) -> None:
    """
    Time:
        best: O(n)
        average: O(n^2)
        worst: O(n^2)
    Space:
        O(1)
        in place
    можно ускорить через введение флага swap = False
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 

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
        bubble_sort(arr)

        assert arr == arr_sorted, f'{arr}'
