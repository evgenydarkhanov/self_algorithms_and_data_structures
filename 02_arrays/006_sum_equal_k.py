# в отсортированном массиве найти
# два элемента, сумма которых равна k

from typing import List, Optional, Tuple


def find_sum_k(arr: List[int], k: int) -> Optional[Tuple[int, int]]:
    """O(n), two pointers"""
    l = 0
    r = len(arr) - 1
    while l < r:
        summ = arr[l] + arr[r]
        if summ < k:
            l += 1
        elif summ > k:
            r -= 1
        else:
            return (l, r)
    return None


if __name__ == "__main__":
    arr = list(range(10))

    assert find_sum_k(arr, 1) == (0, 1)
    assert find_sum_k(arr, 9) == (0, 9)
    assert find_sum_k(arr, 10) == (1, 9)
    assert find_sum_k(arr, 11) == (2, 9)
    assert find_sum_k(arr, 5) == (0, 5)
    assert find_sum_k(arr, 20) is None
