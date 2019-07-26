# -*- coding: utf-8 -*-
#!/usr/bin/env python

from unittest import TestCase, main
from adj_matrix import check_path

class TestAdjMatrix(TestCase):

    def test_check_paths(self):
        arrarr = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        self.assertTrue(check_path(arrarr, "ABCCED"))
        self.assertTrue(check_path(arrarr, "SEE"))
        self.assertFalse(check_path(arrarr, "ABCB"))
        self.assertFalse(check_path(arrarr, "ABA"))
        self.assertFalse(check_path(arrarr, "ABCEED"))
        self.assertFalse(check_path(arrarr, "ABCCFB"))


if __name__ == '__main__':
    main()
