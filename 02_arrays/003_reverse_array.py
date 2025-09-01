from typing import Any, List


def reverse_list(arr: List[Any]) -> None:
    """O(n), in place"""
    length = len(arr)
    for i in range(length // 2):
        arr[i], arr[length - i - 1] = arr[length - i - 1], arr[i]


if __name__ == "__main__":
    lst = list(range(10))
    reverse_list(lst)
    assert lst == list(range(9, -1, -1))    

    lst = list(range(9))
    reverse_list(lst)
    assert lst == list(range(8, -1, -1))

    lst = []
    reverse_list(lst)
    assert lst == []

    lst = [0]
    reverse_list(lst)
    assert lst == [0]

    lst = [0, 1]
    reverse_list(lst)
    assert lst == [1, 0]
