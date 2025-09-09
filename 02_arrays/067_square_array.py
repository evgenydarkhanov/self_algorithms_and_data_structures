# дан неубывающий массив целых чисел, вернуть неубывающий массив квадратов чисел

from typing import List


def square_array(nums: List[int]) -> List[int]:
    l = r = 0
    for idx, elem in enumerate(nums):
        if elem >= 0:
            r = idx
            l = idx - 1
            break

    out = []
    n = len(nums)
    while l > -1 and r < n:
        if nums[l]**2 <= nums[r]**2:
            out.append(nums[l]**2)
            l -= 1
        else:
            out.append(nums[r]**2)
            r += 1

    while l > -1:
        out.append(nums[l]**2)
        l -= 1
    while r < n:
        out.append(nums[r]**2)
        r += 1

    return out


if __name__ == "__main__":
    nums = [-10, -8, -4, 0, 4, 9]
    assert square_array(nums) == [0, 16, 16, 64, 81, 100], square_array(nums)
