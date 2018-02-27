"""
Directions:
    Given a string str, reverse it and return it. Should perform the same action as str[::-1].
"""


def reverse(str):
    rev_str = [x for x in reversed(str)]
    return ''.join(rev_str)
