"""
Directions:
    Given a string, return true if the reversed string is equal to the original, false otherwise.
"""


def palindrome(str):
    rev_str = [x for x in reversed(str)]
    result = map(lambda x: x[0] == x[1], zip(str, rev_str))
    return all(result)


"""
Much easier solution (wanted to practice built-ins above):

def palindrome(str):
    rev_str = [x for x in reversed(str)]
    return str == rev_str
"""
