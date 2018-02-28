"""
Directions: Oh, the classic FizzBuzz problem! Write a program that, for integers from 1 to n, returns the string
    evaluation of the integer. However, if the integer is divisible by 3, return "fizz", or if it is divisible by 5,
    return "buzz". If the integer is divisible by both 3 and 5, then return "fizzbuzz"

    For the input argument n, return a list of size n - 1 that makes the substitutions described above.
"""


def fizzbuzz(n):
    def operate(num):
        if num % 5 == 0 and num % 3 == 0:
            return 'fizzbuzz'
        elif num % 3 == 0:
            return 'fizz'
        elif num % 5 == 0:
            return 'buzz'
        return str(num)

    return [operate(x) for x in range(1, n + 1)]
