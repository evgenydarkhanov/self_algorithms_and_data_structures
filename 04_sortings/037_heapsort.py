import heapq
import random
from typing import Any, List


def heapsort(arr: List[Any]) -> List[Any]:
    if not arr:
        return []

    h = []
    for elem in arr:
        heapq.heappush(h, elem)

    return [heapq.heappop(h) for _ in range(len(h))]


def heapsort_2(arr: List[Any]) -> List[Any]:
    if not arr:
        return []

    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


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
        arr_custom = heapsort(arr)
        arr_custom_2 = heapsort_2(arr)

        assert arr_custom == arr_reference == arr_custom_2, f'{arr_custom}\n{arr_custom_2}'
