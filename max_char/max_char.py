"""
Directions:
    Given a string, return the most frequently occurring character. Don't worry about duplicates.
"""


def max_char(str):
    char_counts = {}
    max_char = str[0]
    max_count = 0

    for char in str:
        char_counts[char] = char_counts.get(char, 0) + 1
        if char_counts[char] > max_count:
            max_count = char_counts[char]
            max_char = char

    return max_char