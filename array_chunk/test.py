from array_chunk import array_chunk
import unittest


class TestArrayChunkOne(unittest.TestCase):
    def setUp(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.chunked = array_chunk(arr, 2)

    def test_equal(self):
        self.assertEqual(self.chunked, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
                         'divides an array of 10 elements into chunks of 2')


class TestArrayChunkTwo(unittest.TestCase):
    def setUp(self):
        arr = [1, 2, 3]
        self.chunked = array_chunk(arr, 1)

    def test_equal(self):
        self.assertEqual(self.chunked, [[1], [2], [3]],
                         'divides an array of 3 elements into chunks of 1')


class TestArrayChunkThree(unittest.TestCase):
    def setUp(self):
        arr = [1, 2, 3, 4, 5]
        self.chunked = array_chunk(arr, 3)

    def test_equal(self):
        self.assertEqual(self.chunked, [[1, 2, 3], [4, 5]],
                         'divides an array of 5 elements into chunks of 3')


class TestArrayChunkFour(unittest.TestCase):
    def setUp(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.chunked = array_chunk(arr, 5)

    def test_equal(self):
        self.assertEqual(self.chunked, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]],
                         'divides an array of 13 elements into chunks of 5')


if __name__ == '__main__':
    unittest.main()
