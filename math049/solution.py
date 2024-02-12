"""
    Math 49
"""


def is_prime(num):
    """
    Check primeness of a number.
    """
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def answer():
    """
    answer().
    """
    primes = [
        number for number in range(1000, 10000) if is_prime(number) and number != 1487
    ]
    num_str = ""

    for prime in primes:
        if prime > 3500:
            break

        mid = prime + 3330
        large = mid + 3330

        if mid in primes and large in primes:
            num_str = str(prime) + str(mid) + str(large)
            break

    return num_str


if __name__ == "__main__":
    print(f"answer()={answer()}")
