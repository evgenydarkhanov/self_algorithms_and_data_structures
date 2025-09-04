# на вход массив целых чисел
# вернуть массив с числами, являющимися произведением всех кроме данного
# [1, 2, 10, 3] --> [60, 30, 6, 20]
# [1, 5, 0, 3] --> [0, 0, 15, 0]
# используем произведение чисел справа и слева, кроме самого числа

from typing import List


def product_array(nums: List[int]) -> List[int]:
    n = len(arr)
    out = [0 for _ in range(n)]
    prod = 1

    for i in range(n):
        out[i] = prod
        prod *= arr[i]

    prod = 1
    for i in range(n - 1, -1, -1):
        out[i] = prod
        prod *= arr[i]

    return out


if __name__ == "__main__":
    assert product_array([1, 2, 10, 3]) == [60, 30, 6, 20]
    assert product_array([1, 5, 0, 3]) == [0, 0, 15, 0]
