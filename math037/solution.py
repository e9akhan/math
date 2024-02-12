"""
    Find the sum of the only eleven primes that are both truncatable
    from left to right and right to left.
"""


def is_prime(number):
    """
    Check for primeness of number.
    """
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def rounding(number):
    """
    Check truncable primeness.
    """
    temp = str(number)

    truncatable_prime = []
    for i in range(1, len(temp)):
        numl = temp[i:]
        numr = temp[:-i]

        truncatable_prime.append(is_prime(int(numl)))
        truncatable_prime.append(is_prime(int(numr)))

    if False in truncatable_prime:
        return False
    return True


def solver(n):
    """
    Find the sum of n truncable prime numbers from both sides.
    """
    cyclic_primes = []

    number = 23
    while len(cyclic_primes) < n:
        if not is_prime(number):
            number += 1
            continue

        if rounding(number):
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
