# вход: массив чисел и число k
# вернуть индексы двух чисел, сумма которых даёт k
# nums[i] + nums[j] = k
# массив не отсортирован, int'ы
# O(n^2) - перебор двумя указателями
# O(nlogn) - отсортировать и двумя указателями
# O(n) - со словарём


from typing import List, Optional, Tuple


def sum_equal_k(nums: List[int], k: int) -> List:
    if len(nums) < 2:
        return []

    cache = {}
    for i, num in enumerate(nums):
        compl = k - num
        if compl in cache:
            # вернём индексы в порядке возрастания
            return [cache[compl], i]

        cache[num] = i

    return []


if __name__ == "__main__":
    assert sum_equal_k([], 5) == [], f"{sum_equal_k([], 5) = }"
    assert sum_equal_k([1], 5) == [], f"{sum_equal_k([1], 5) = }"
    assert sum_equal_k([1, 2, 3], 9) == [], f"{sum_equal_k([1, 2, 3], 9) = }"
    # assert sum_equal_k([0, 1, 2, 3, 4, 5], 7) == [2, 5], f"{sum_equal_k([0, 1, 2, 3, 4, 5], 7) = }"
    assert sum_equal_k([2, 3], 5) == [0, 1], f"{sum_equal_k([2, 3], 5) = }"
    assert sum_equal_k([1, 1], 2) == [0, 1], f"{sum_equal_k([1, 1], 2) = }"
