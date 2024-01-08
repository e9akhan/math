"""
    Module name :- solution
    Method(s) :- solver(n), is_prime(number), answer()
"""


def is_prime(number):
    """
    Checks whether the given number is prime or not.

    Args:
        number(int) :- Number whose primeness to check.

    Return:
        True if number is prime else False
    """
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def solver(n: int):
    """
    Find the nth prime number.
    """
    count = 1
    prime = -1
    number = 2

    while count <= n:
        if is_prime(number):
            prime = number
            count += 1
        number += 1
    return prime


def answer():
    """
    Find the 10001st prime number
    """
    return solver(10001)


if __name__ == "__main__":
    print(f"solver(168) = {solver(168)}")
    print(f"answer() = {answer()}")
