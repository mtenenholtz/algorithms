from palindrome import palindrome
import unittest


class TestPalindrome(unittest.TestCase):
    def test_one(self):
        self.assertTrue(palindrome('aba'), '"aba" is a palindrome')


    def test_two(self):
        self.assertFalse(palindrome(' aba'), '" aba" is not a palindrome')


    def test_three(self):
        self.assertFalse(palindrome('aba '), '"aba " is not a palindrome')


    def test_four(self):
        self.assertFalse(palindrome('greetings'), '"greetings" is a palindrome')


    def test_five(self):
        self.assertTrue(palindrome('1000000001'), '"1000000001" is a palindrome')


    def test_six(self):
        self.assertFalse(palindrome('Fish hsif'), '"Fish hsif" is not a palindrome')


    def test_seven(self):
        self.assertTrue(palindrome('fish hsif'), '"fish hsif" is a palindrome')


    def test_eight(self):
        self.assertTrue(palindrome('racecar'), '"racecar" is a palindrome')


if __name__ == '__main__':
    unittest.main()
