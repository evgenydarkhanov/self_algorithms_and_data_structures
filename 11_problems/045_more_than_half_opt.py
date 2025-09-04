# функция принимает на вход массив элементов
# одно из чисел занимает больше половины массива
# найти это число
# [1, 2, 1, 3, 1] == 1
# [1, 1, 2] == 1
# попробуем за О(1) по памяти
# если это число встречается больше половины раз, то его количество не может быть нивелировано
# проблема с последним тестом

from typing import List, Optional


def find_more_than_half(nums: List[int]) -> Optional[int]:
    value = None
    count = 0
    for num in nums:
        # начинаем заново, если полностью нивелировали
        if count == 0:
            value = num
        if num == value:
            count += 1
        else:
            count -= 1

    return value


if __name__ == "__main__":
    assert find_more_than_half([1, 2, 1, 3, 1]), f"{find_more_than_half([1, 2, 1, 3, 1]) = }"
    assert find_more_than_half([1, 1, 2]), f"{find_more_than_half([1, 1, 2]) = }"
    assert find_more_than_half([1, 2, 3]) is None, f"{find_more_than_half([1, 2, 3]) = }"
