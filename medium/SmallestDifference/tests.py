import unittest

from medium.SmallestDifference.solution import smallest_difference


class TestThreeNumberSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(smallest_difference(
            [-1, 5, 10, 20, 28, 3],
            [26, 134, 135, 15, 17]),
            [28, 26]
        )

    def test2(self):
        self.assertEqual(smallest_difference(
            [-1, 5, 10, 20, 3],
            [26, 134, 135, 15, 17]),
            [20, 17]
        )

    def test3(self):
        self.assertEqual(smallest_difference(
            [10, 0, 20, 25],
            [1005, 1006, 1014, 1032, 1031]),
            [25, 1005]
        )

    def test4(self):
        self.assertEqual(smallest_difference(
            [10, 0, 20, 25, 2200],
            [1005, 1006, 1014, 1032, 1031]),
            [25, 1005]
        )

    def test5(self):
        self.assertEqual(smallest_difference(
            [10, 0, 20, 25, 2000],
            [1005, 1006, 1014, 1032, 1031]),
            [2000, 1032]
        )

    def test6(self):
        self.assertEqual(smallest_difference(
            [240, 124, 86, 111, 2, 84, 954, 27, 89],
            [1, 3, 954, 19, 8]),
            [954, 954]
        )

    def test7(self):
        self.assertEqual(smallest_difference(
            [0, 20],
            [21, -2]),
            [20, 21]
        )

    def test8(self):
        self.assertEqual(smallest_difference(
            [10, 1000],
            [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]),
            [1000, 1014]
        )

    def test9(self):
        self.assertEqual(smallest_difference(
            [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123],
            [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]),
            [-123, -124]
        )

    def test10(self):
        self.assertEqual(smallest_difference(
            [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530],
            [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]),
            [530, 530]
        )