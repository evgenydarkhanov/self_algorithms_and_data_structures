# несортированный массив целых чисел, перенести в начало четные числа устойчиво

from typing import List


def forward_evens(nums: List[int]) -> List[int]:
    odds = []
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    return evens + odds
                                                                                    

if __name__ == "__main__":
    assert forward_evens([3, 2, 4, 1, 11, 8, 9]) == [2, 4, 8, 3, 1, 11, 9]
    assert forward_evens([7, 2, 5, 8, 1, 6, 3, 4]) == [2, 8, 6, 4, 7, 5, 1, 3]
