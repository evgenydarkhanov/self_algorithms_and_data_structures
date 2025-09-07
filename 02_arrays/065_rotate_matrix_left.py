from typing import List, NewType


Matrix = NewType("Matrix", List[List[int]])


def rotate_matrix_left(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)][::-1]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rot_matrix = [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ]

    assert rotate_matrix_left(matrix) == rot_matrix, rotate_matrix_left(matrix)
    assert rotate_matrix_left([[1]]) == [[1]], rotate_matrix_left([[1]])
    assert rotate_matrix_left([[0, 1]]) == [[1], [0]], rotate_matrix_left([[0], [1]])
    assert rotate_matrix_left([[0, 1], [2, 3]]) == [[1, 3], [0, 2]], rotate_matrix_left([[2, 0], [3, 1]])
