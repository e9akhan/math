"""
    Find the sum of the only eleven primes that are both truncatable
    from left to right and right to left.
"""


def is_prime(number):
    """
    Check for primeness of number.
    """
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def rounding(number, left=True):
    """
    Check truncable primeness.
    """
    count = 1
    temp = str(number)[::-1]

    if left:
        number = int(temp)
    number //= 10

    while number > 0 and is_prime(number):
        count += 1
        number //= 10

    if count == len(temp):
        return True
    return False


def solver(n):
    """
    Find the sum of n truncable prime numbers from both sides.
    """
    cyclic_primes = []

    number = 10
    while len(cyclic_primes) < n:
        if not is_prime(number):
            number += 1
            continue

        if rounding(number) and rounding(number, left=False):
            cyclic_primes.append(number)

        number += 1

    return sum(cyclic_primes)


def answer():
    """
    Find the sum of the only eleven primes that are both truncatable
    from left to right and right to left.
    """
    return solver(11)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
