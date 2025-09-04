# функция принимает на вход массив элементов
# одно из чисел занимает больше половины массива
# найти это число
# [1, 2, 1, 3, 1] == 1
# [1, 1, 2] == 1

from typing import List, Optional


def find_more_than_half(nums: List[int]) -> Optional[int]:

    # можно через defaultdict
    dct = {}
    for num in nums:
        if num not in dct:
            dct[num] = 1
        else:
            dct[num] += 1

    max_key, max_val = max(dct.items(), key=lambda x: x[1])

    if max_val > (len(nums) // 2):
        return max_key

    return None


if __name__ == "__main__":
    assert find_more_than_half([1, 2, 1, 3, 1]), f"{find_more_than_half([1, 2, 1, 3, 1]) = }"
    assert find_more_than_half([1, 1, 2]), f"{find_more_than_half([1, 1, 2]) = }"
    assert find_more_than_half([1, 2, 3]) is None, f"{find_more_than_half([1, 2, 3]) = }"
