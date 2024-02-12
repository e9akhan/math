"""
    Find the first n consecutive number to have n distinct
    prime factors each.
"""


def find_consecutive_numbers_with_distinct_prime(num, n, prime_list):
    """
    Check whether the number and its n consective has n
    distinct prime factors
    """
    if num in prime_list:
        return False

    for number in range(num, num + n):
        used_prime_number = []
        for prime in prime_list:
            if prime in used_prime_number:
                continue

            if number % prime == 0:
                used_prime_number.append(prime)

        if len(used_prime_number) != n:
            return False
    return True


def is_prime(num):
    """
    Check primeness of a number.
    """
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def solver(n):
    """
    Find the first n consecutive number to have n distinct
    prime factors each.
    """
    number = 3
    prime_list = [2]
    while not find_consecutive_numbers_with_distinct_prime(number, n, prime_list):
        if is_prime(number):
            prime_list.append(number)

        number += 1

    return number


def answer():
    """
    Find the first 4 consecutive number to have 4 distinct
    prime factors each.
    """
    return solver(4)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
