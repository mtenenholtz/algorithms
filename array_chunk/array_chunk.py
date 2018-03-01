"""
Directions:
    Given an array and chunk size, divide the array into many subarrays where each subarray is of length size

Examples:
    chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
    chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
    chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
    chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
    chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
"""


def array_chunk(array, size):
    offset = 0
    chunked_array = []

    while offset + size < len(array):
        chunked_array.append(array[offset:offset + size])
        offset += size

    chunked_array.append(array[offset:])
    return chunked_array
