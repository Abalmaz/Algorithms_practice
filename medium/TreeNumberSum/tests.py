import unittest

from medium.TreeNumberSum.solution import three_number_sum


class TestThreeNumberSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6],[-8, 3, 5], [-6, 1, 5]])

    def test2(self):
        self.assertEqual(three_number_sum([1, 2, 3], 6), [[1, 2, 3]])

    def test3(self):
        self.assertEqual(three_number_sum([1, 2, 3], 7), [])

    def test4(self):
        self.assertEqual(three_number_sum([8, 10, -2, 49, 14], 57), [[-2, 10, 49]])

    def test5(self):
        self.assertEqual(three_number_sum([12, 3, 1, 2, -6, 5, 0, -8, -1], 0), [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]])

    def test6(self):
        self.assertEqual(three_number_sum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]])

    def test7(self):
        self.assertEqual(three_number_sum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-5, -1, 6], [-5, 0, 5], [-5, 2, 3], [-1, 0, 1]])

    def test8(self):
        self.assertEqual(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18), [[1, 2, 15], [1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]])

    def test9(self):
        self.assertEqual(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32), [[8, 9, 15]])

    def test10(self):
        self.assertEqual(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33), [])

    def test11(self):
        self.assertEqual(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5), [])