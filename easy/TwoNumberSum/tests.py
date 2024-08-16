import unittest

from easy.TwoNumberSum.solution import two_number_sum


class TestTwoNumberSum(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(two_number_sum(
            [3, 5, -4, 8, 11, 1, -1, 6], 10),
            [-1, 11]
        )

    def test2(self):
        self.assertCountEqual(two_number_sum(
            [4, 6], 10),
            [4, 6]
        )

    def test3(self):
        self.assertCountEqual(two_number_sum(
            [4, 6, 1], 5),
            [4, 1]
        )

    def test4(self):
        self.assertCountEqual(two_number_sum(
            [4, 6, 1, -3], 3),
            [6, -3]
        )

    def test5(self):
        self.assertCountEqual(two_number_sum(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18),
            [3, 15]
        )

    def test6(self):
        self.assertCountEqual(two_number_sum(
            [-7, -5, -3, -1, 0, 1, 3, 5, 7], -5),
            [-5, 0]
        )

    def test7(self):
        self.assertCountEqual(two_number_sum(
            [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163),
            [210, -47]
        )

    def test8(self):
        self.assertCountEqual(two_number_sum(
            [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164),
            []
        )

    def test9(self):
        self.assertCountEqual(two_number_sum(
            [3, 5, -4, 8, 11, 1, -1, 6], 15),
            []
        )

    def test10(self):
        self.assertCountEqual(two_number_sum(
            [14], 15),
            []
        )

    def test11(self):
        self.assertCountEqual(two_number_sum(
            [15], 15),
            []
        )

    def test12(self):
        self.assertCountEqual(two_number_sum(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 17),
            [8, 9]
        )