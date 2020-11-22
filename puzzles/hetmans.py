# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np


def print_chess(matrix_size, hetmans):
    matrix = np.zeros((matrix_size, matrix_size))
    for i in range(len(hetmans)):
        matrix[i, hetmans[i]] = 1
    print(matrix)


def set_hetmans(hetmans,
                selected_columns,
                matrix_size,
                diagonal_left,
                diagonal_right):
    row = len(hetmans)
    if row == matrix_size:
        return True
    for new_col in range(matrix_size):
        left_diagonal_index = row + new_col
        right_diagonal_index = 7 + row - new_col
        if new_col not in selected_columns and \
                left_diagonal_index not in diagonal_left and \
                right_diagonal_index not in diagonal_right:
            hetmans += [new_col]
            selected_columns[new_col] = True
            diagonal_left[left_diagonal_index] = True
            diagonal_right[right_diagonal_index] = True

            if set_hetmans(hetmans,
                           selected_columns,
                           matrix_size,
                           diagonal_left,
                           diagonal_right):
                return True

            hetmans.pop()
            del selected_columns[new_col]
            del diagonal_left[left_diagonal_index]
            del diagonal_right[right_diagonal_index]
        else:
            new_col += 1
    return False


def main():
    matrix_size = 8
    hetmans = []
    selected_columns = {}
    diagonal_left = {}
    diagonal_right = {}
    set_hetmans(hetmans,
                selected_columns,
                matrix_size,
                diagonal_left,
                diagonal_right)
    print_chess(matrix_size, hetmans)


if __name__ == '__main__':
    main()
