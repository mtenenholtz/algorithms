from reverse_string import reverse
import unittest


class TestReverseString(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('abcd'), 'dcba')


    def test_reverse_with_whitespace(self):
        self.assertEqual(reverse('  abcd'), 'dcba  ')


if __name__ == '__main__':
    unittest.main()