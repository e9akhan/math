"""
    Module name :- solution
    Method(s) :- is_prime(number), solver(p, q), answer()
"""


def is_prime(number):
    """
    Check whether the number is prime or non-prime.

    Args:-
        number(int) :- Integer number to check primeness.

    Return
        True if number is prime else False.
    """
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def solver(p: int, q: int = None):
    """
    Find the sum of prime numbers between a range.

    Args:-
        p(int) :- Starting point of the range.
        q(int) :- Ending point of the range.

    Return:
        Sum of the prime number over the given range.
    """

    if p < 0:
        return None

    start = 2
    end = p

    if q:
        start = p
        end = q

    if start > end:
        return None

    sum_prime = 0

    for i in range(start, end):
        if is_prime(i):
            sum_prime += i

    return sum_prime


def answer():
    """
    Find the sum of prime numbers upto 2000000.

    Return
        Sum of prime numbers upto 2000000
    """
    return solver(2000000)


if __name__ == "__main__":
    print(f"solver(10) = {solver(10)}")
    print(f"answer() = {answer()}")
