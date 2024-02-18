"""
    Math 69
"""


def is_prime(num):
    """
    Check whether the number is prime or not.
    """
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def gcd(x, y):
    """
    Find GCD of x and y.
    """
    return y and gcd(y, x % y) or x


def solver(n):
    """
    Find the number which has maximum number to relative prime ratio.
    """
    if n < 2:
        return n

    totient_number = 0
    maximum = 0

    for i in range(2, n + 1):
        if is_prime(i):
            continue

        count = 0

        for j in range(1, i):
            if gcd(i, j) == 1:
                count += 1
        val = i / count

        if maximum < val:
            totient_number = i

    return totient_number


def answer():
    """
    Find the number which has maximum number to relative prime ratio upto 1e6.
    """
    return solver(1000000)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
