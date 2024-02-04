"""
    Math 033
"""

from math import prod


def gcd(x, y):
    """
    Find gcd of two numbers.
    """
    return y and gcd(y, x % y) or x


def solver():
    """
    If the product of non trivial solution of 2 digit number is given in its lowest
    common terms, find the value of the denominator.
    """
    numerator_list, denominator_list = [], []
    for i in range(10, 99):
        if i % 10 == 0:
            continue

        for j in range(i + 1, 100):
            if j % 10 == 0:
                continue

            str_i, str_j = str(i), str(j)
            set_i, set_j = set(str_i), set(str_j)
            common = set_i & set_j

            if common and len(set_i) == len(str_i) and len(set_j) == len(str_j):
                numerator = "".join([digit for digit in str_i if digit not in common])
                denominator = "".join([digit for digit in str_j if digit not in common])

                if not numerator or not denominator:
                    continue

                numerator, denominator = int(numerator), int(denominator)

                is_non_trivial = numerator / denominator == i / j

                if is_non_trivial:
                    greatest_divisor = gcd(denominator, numerator)
                    numerator_list.append(numerator // greatest_divisor)

                    denominator_value = denominator // greatest_divisor

                    if denominator_value in numerator_list:
                        numerator_list.remove(denominator_value)
                        continue

                    denominator_list.append(denominator_value)

    return prod(denominator_list)


def answer():
    """
    If the product of non trivial solution of 2 digit number is given in its lowest
    common terms, find the value of the denominator.
    """
    return solver()
