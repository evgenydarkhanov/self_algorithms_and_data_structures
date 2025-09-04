# на вход массив целых чисел
# вернуть массив с числами, являющимися произведением всех кроме данного
# [1, 2, 10, 3] --> [60, 30, 6, 20]
# [1, 5, 0, 3] --> [0, 0, 15, 0]

from typing import List


def product_array(nums: List[int]) -> List[int]:
    zeros = 0
    prod = 1
    for num in nums:
        if num == 0:
            zeros += 1
        else:
            prod *= num

    if zeros == 0:
        return [prod / elem for elem in nums]

    elif zeros == 1:
        return [0 if elem != 0 else prod for elem in nums]

    return [0 for _ in range(len(nums))]


if __name__ == "__main__":
    assert product_array([1, 2, 10, 3]) == [60, 30, 6, 20]
    assert product_array([1, 5, 0, 3]) == [0, 0, 15, 0]
