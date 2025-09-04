# на вход массив чисел, каждое число - максимальное количество, на которое можно прыгнуть
# e. g. "3" --> можем прыгнуть на 0, 1 или 2
# можем ли мы добраться до последней ячейки?
# [2, 3, 1, 1, 4] - True
# [2, 3, 1, 1, 0, 4] - False

from typing import List


def can_jump(arr: List[int]) -> bool:
    n = len(arr)
    if n <= 1:
        return True

    # максимальный индекс, до которого можем добраться
    max_reach = 0

    for i in range(n):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + arr[i])

        if max_reach >= (n - 1):
            return True

    return False


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]), f"{can_jump([2, 3, 1, 1, 4]) = }"
    assert not can_jump([2, 3, 1, 1, 0, 4]), f"{can_jump([2, 3, 1, 1, 0, 4]) = }"
    assert not can_jump([0, 1, 2, 3]), f"{can_jump([0, 1, 2, 3]) = }"
    assert can_jump([0])
    assert not can_jump([0, 1])
    assert can_jump([1, 0])
    assert not can_jump([1, 0, 0])
    assert can_jump([2, 0, 0])
    assert not can_jump([1, 0, 2])
    assert can_jump([2, 0, 1, 0])
