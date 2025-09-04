# массив чисел, каждое число означает высоту столба
# между столбами наливается вода
# найти наибольший объём воды
# например, [1, 8, 6, 2, 5, 4, 8, 3, 7] = 49
#
#   |_ _ _ _ _|_ _
#   |         |   |
#   | |       |   |
#   | |   |   |   | 
#   | |   | | |   |
#   | |   | | | | |
#   | | | | | | | |
# | | | | | | | | |
# —————————————————
# 1 8 6 2 5 4 8 3 7
# можно решать двумя указателями жадно

from typing import List


def most_water(arr: List[int]) -> int:
    l = 0
    r = len(arr) - 1
    max_area = 0
    while l != r:
        w = r - l
        h = min(arr[l], arr[r])
        # if h * w > max_area:
        #    max_area = h * w
        max_area = max(max_area, h * w)

        # сдвигаем меньший указатель
        if arr[l] <= arr[r]:
            l += 1
        else:
            r -= 1

    return max_area


if __name__ == "__main__":
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert most_water(nums) == 49, f"{most_water(nums) = }"
