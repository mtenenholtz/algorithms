from reverse_int import reverse_int
import unittest


class TestPalindrome(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(reverse_int(0), 0, "handles zero properly")

    def test_positives(self):
        self.assertEqual(reverse_int(5), 5)
        self.assertEqual(reverse_int(15), 51)
        self.assertEqual(reverse_int(90), 9)
        self.assertEqual(reverse_int(2359), 9532)

    def test_negatives(self):
        self.assertEqual(reverse_int(-5), -5)
        self.assertEqual(reverse_int(-15), -51)
        self.assertEqual(reverse_int(-90), -9)
        self.assertEqual(reverse_int(-2359), -9532)


if __name__ == '__main__':
    unittest.main()
