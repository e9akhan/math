"""
    Module name :- solution
    Method(s) :- solver(p, q), answer()
"""

from math import prod


def solver(p: int, q: int = None):
    """
    Returns dictionary of list of tuples containing pythagorean
    triplets as value and their sum as keys.

    Args:
        p(int) :- Starting point of a number
        q(int) :- Ending point of a number.

    Return:
        Dictionary of list of tuples
    """
    start = 1
    end = p

    if q:
        start = p
        end = q

    if start > end:
        return -1

    dictionary = {}

    for i in range(start, end + 1):
        for a in range(1, i // 3):
            c = (i**2 - 2 * i * a + 2 * (a**2)) // (2 * (i - a))
            b = i - a - c

            if a**2 + b**2 == c**2:
                total = i
                if total in dictionary:
                    dictionary[total] += [(a, b, c)]
                else:
                    dictionary[total] = [(a, b, c)]

    return dictionary


def answer():
    """
    Find product of pythagorean triplet of sum of 1000.

    Return
        Product of pythagorean triplet of sum of 1000.
    """

    dictionary = solver(1000, 1000)
    values = list(dictionary.values())[0][0]

    return prod(values)


if __name__ == "__main__":
    print(f"solver(12) = {solver(12)}")
    print(f"answer() = {answer()}")
