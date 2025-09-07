# массив неотсортированных целых чисел, вернуть первое с конца четное

from typing import List, Optional


def get_last_even(nums: List[int]) -> Optional[int]:
    while nums:
        num = nums.pop()
        if num % 2 == 0:
            return num
    return None


if __name__ == "__main__":
    assert get_last_even([8, 9, 10, 16, 9]) == 16
    assert get_last_even([8, 9, 11, 17, 9]) == 8
    assert get_last_even([9, 9, 11, 13, 9]) is None
    assert get_last_even([]) is None
