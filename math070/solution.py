"""
    Math 70
"""


def gcd(x, y):
    """
    GCD of x and y.
    """
    return y and gcd(y, x % y) or x


def is_permutation(num1, num2):
    """
    Is num1 and num2 permutation of eachh other.
    """
    return sorted(str(num1)) == sorted(str(num2))


def solver(n):
    """
    solver().
    """
    if n < 2:
        return n

    totient_number = 0
    maximum = 100000000

    for i in range(2, n):
        count = 0

        for j in range(1, i):
            if gcd(i, j) != 1:
                continue

            count += 1

        if is_permutation(i, count):
            val = i / count
            if val < maximum:
                totient_number = i

    return totient_number


def answer():
    """
    answer()
    """
    return solver(87500)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
