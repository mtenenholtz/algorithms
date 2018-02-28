from fizzbuzz import fizzbuzz
import unittest


class TestFizzBuzzFive(unittest.TestCase):
    def setUp(self):
        self.sequence = ['1', '2', 'fizz', '4', 'buzz']

    def test_equal(self):
        self.assertEqual(fizzbuzz(5), self.sequence)


class TestFizzBuzzFifteen(unittest.TestCase):
    def setUp(self):
        self.sequence = [
            '1',
            '2',
            'fizz',
            '4',
            'buzz',
            'fizz',
            '7',
            '8',
            'fizz',
            'buzz',
            '11',
            'fizz',
            '13',
            '14',
            'fizzbuzz'
        ]

    def test_equal(self):
        self.assertEqual(fizzbuzz(15), self.sequence)


if __name__ == '__main__':
    unittest.main()
