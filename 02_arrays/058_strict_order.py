"""
Дан массив целых чисел nums. Нужно вернуть длину наибольшего подмассива чисел,
который либо строго возрастает либо строго убывает.
Строго означает, что применяется строгое неравенство
"""

from typing import List


def strict_order(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return 1
    if n == 2:
        if nums[0] != nums[1]:
            return 2
        return 1

    max_length, cnt_inc, cnt_dec = 0, 1, 1
    l, r = 0, 1

    while r < n:
        if nums[l] < nums[r]:
            cnt_inc += 1
            max_length = max(max_length, cnt_inc)
            l += 1
            r += 1

        elif nums[l] > nums[r]:
            cnt_dec += 1
            max_length = max(max_length, cnt_dec)
            l += 1
            r += 1

        else:
            r += 1
            l += 1

    return max_length


if __name__ == "__main__":
    assert strict_order([1, 2, 4, 5]) == 4, f"{strict_order([1, 2, 4, 5]) = }"
    assert strict_order([3, 2, 1]) == 3, f"{strict_order([3, 2, 1]) = }"
    assert strict_order([1, 2, 2, 1]) == 2, f"{strict_order([1, 2, 2, 1]) = }"
    assert strict_order([1]) == 1, f"{strict_order([1]) = }"
    assert strict_order([1, 1]) == 1, f"{strict_order([1, 1]) = }"
    assert strict_order([1, 2, 3, 4, 4, 4, 5, 4, 3, 2, 1, 0]) == 6, f"{strict_order([1, 2, 3, 4, 4, 4, 5, 4, 3, 2, 1, 0]) = }"
