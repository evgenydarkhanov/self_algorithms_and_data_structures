# обойти матрицу улиткой

from typing import List, NewType


Matrix = NewType("Matrix", List[List[int]])


def snail_matrix(matrix: Matrix) -> List[int]:
    result = []

    l, r = 0, len(matrix[0]) - 1
    t, b = 0, len(matrix) - 1

    while l <= r and t <= b:
        # >
        for i in range(l, r + 1):
            result.append(matrix[t][i])
        t += 1

        # v
        for i in range(t, b + 1):
            result.append(matrix[i][r])
        r -= 1

        # <
        if t <= b:
            for i in range(r, l - 1, -1):
                result.append(matrix[b][i])
            b -= 1

        # ^
        if l <= r:
            for i in range(b, t - 1, -1):
                result.append(matrix[i][l])
            l += 1

    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    result = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    assert snail_matrix(matrix) == result, snail_matrix(matrix)
