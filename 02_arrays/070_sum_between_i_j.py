# дан массив чисел, найти сумму всех элементов между индексами i и j за O(1)
# используем префиксные суммы

from typing import List


def calculate_prefix_sum(arr: List[int]) -> List[int]:
    ps = arr[:]
    for i in range(1, len(arr)):
        ps[i] += ps[i - 1]
    return ps


def sum_i_j(arr: List[int], i: int, j: int) -> int:
    prefix_sum = calculate_prefix_sum(arr)
    return prefix_sum[j - 1] - prefix_sum[i]


if __name__ == "__main__":
    assert sum_i_j([0, 1, 2, 3, 4], 0, 4) == 6, sum_i_j([0, 1, 2, 3, 4], 0, 4)
    assert sum_i_j([0, 1, 2, 3, 4], 0, 3) == 3, sum_i_j([0, 1, 2, 3, 4], 0, 3)
    assert sum_i_j([9, 8, 7, 6, 5, 4, 3], 3, 6) == 9, sum_i_j([9, 8, 7, 6, 5, 4, 3], 3, 6)
    assert sum_i_j([1, 1, 1, 1, 1], 2, 4) == 1, sum_i_j([1, 1, 1, 1, 1], 2, 4)
    assert sum_i_j([1, -1, 1, -1, 1, -1], 2, 5) == 0, sum_i_j([1, -1, 1, -1, 1, -1], 2, 5)
