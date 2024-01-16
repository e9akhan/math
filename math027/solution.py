"""
    Quadratic primes
"""


def is_prime(num):
    """
    Check whether the given number is prime or non-prime
    """
    if num > 0:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False


def solver():
    """
    Find the product of the coefficients, and , for the quadratic
    expression that produces the maximum number of primes.
    """
    prime_and_coef_product = {}

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            num = 0
            while is_prime(num**2 + a * num + b):
                num += 1

            prime_and_coef_product.update({num: a * b})

    key = sorted(prime_and_coef_product, reverse=True)[0]

    return prime_and_coef_product[key]


def answer():
    """
    Find the product of the coefficients, and , for the quadratic
    expression that produces the maximum number of primes starting with n=0.
    """
    return solver()


if __name__ == "__main__":
    print(f"anaswer() = {answer()}")
