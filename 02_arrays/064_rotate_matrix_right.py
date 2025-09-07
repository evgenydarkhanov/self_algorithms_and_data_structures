from typing import List, NewType


Matrix = NewType("Matrix", List[List[int]])


def rotate_matrix_right(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix[::-1])]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rot_matrix = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    assert rotate_matrix_right(matrix) == rot_matrix, rotate_matrix_right(matrix)
    assert rotate_matrix_right([[1]]) == [[1]], rotate_matrix_right([[1]])
    assert rotate_matrix_right([[0, 1]]) == [[0], [1]], rotate_matrix_right([[0], [1]])
    assert rotate_matrix_right([[0, 1], [2, 3]]) == [[2, 0], [3, 1]], rotate_matrix_right([[2, 0], [3, 1]])
