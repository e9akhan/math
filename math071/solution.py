"""
    Math 71
"""


def gcd(x, y):
    """
    GCD.
    """
    return y and gcd(y, x % y) or x


def is_prime(n):
    """
    Check whether number is prime or not.
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def solver(n, ele):
    """
    solver(n, ele)
    """
    fractions = []

    if n < 2:
        return 0

    for i in range(2, n + 1):
        if is_prime(i):
            fractions += [f"{j}/{i}" for j in range(1, i)]
            continue

        for j in range(1, i):
            if gcd(i, j) == 1:
                fractions.append(f"{j}/{i}")

    fractions = sorted(fractions, key=lambda x: eval(x))
    return fractions[fractions.index(ele) - 1] if fractions.index(ele) else 0


def answer():
    """
    answer()
    """
    return solver(1000000, "3/7")


if __name__ == "__main__":
    print(f"answer() = {answer()}")
