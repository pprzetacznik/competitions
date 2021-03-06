# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
#
# Given a 2D matrix of letters, find if a given word exists in the matrix.
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally #or vertically neighboring.
#
# For example,
# Given board =
# arrarr = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
#  ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# word = "ABA", -> returns false.

import numpy as np
from unittest import TestCase, main


def check_path_details(matrix, matrix_visited, path, point, matrix_shape):
    if matrix_visited[point]:
        return False
    if not path:
        return True
    new_points = [
        (point[0] + change[0], point[1] + change[1])
        for change in [(-1, 0), (0, -1), (1, 0), (0, 1)]
        if point[0] + change[0] >= 0
        and point[0] + change[0] < matrix_shape[0]
        and point[1] + change[1] >= 0
        and point[1] + change[1] < matrix_shape[1]
    ]
    next_letter, *tail_path = path
    new_points_filtered = [
        point for point in new_points if matrix[point] == next_letter
    ]
    matrix_visited[point] = True
    # print(matrix_visited)
    result = any(
        [
            check_path_details(
                matrix, matrix_visited, tail_path, new_point, matrix_shape
            )
            for new_point in new_points_filtered
        ]
    )
    matrix_visited[point] = False
    return result


def initialize_starting_dictionary(matrix):
    starting_dictionary = {}
    for i in np.ndindex(matrix.shape):
        if matrix[i] in starting_dictionary:
            starting_dictionary[matrix[i]] = starting_dictionary[matrix[i]] + [
                i
            ]
        else:
            starting_dictionary[matrix[i]] = [i]
    return starting_dictionary


def check_path(arrarr, final_path):
    matrix = np.matrix(arrarr)
    matrix_visited = np.zeros(matrix.shape, dtype=bool)
    starting_dictionary = initialize_starting_dictionary(matrix)

    # print(starting_dictionary)
    # print(matrix)

    first_letter, *tail_path = final_path
    return any(
        [
            check_path_details(
                matrix, matrix_visited, tail_path, point, matrix.shape
            )
            for point in starting_dictionary[first_letter]
        ]
    )


class TestAdjMatrix(TestCase):
    def test_check_paths(self):
        arrarr = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        self.assertTrue(check_path(arrarr, "ABCCED"))
        self.assertTrue(check_path(arrarr, "SEE"))
        self.assertFalse(check_path(arrarr, "ABCB"))
        self.assertFalse(check_path(arrarr, "ABA"))
        self.assertFalse(check_path(arrarr, "ABCEED"))
        self.assertFalse(check_path(arrarr, "ABCCFB"))


if __name__ == "__main__":
    main()
