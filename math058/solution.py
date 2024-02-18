"""
    Sum of diagonal elements of spiral matrix.
"""


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


def solver(percent):
    """
        solver
    """
    n = 3
    diagonals = [1]
    count = 0

    while True:
        mid = n // 2

        for _ in range(4):
            ele = diagonals[-1] + 2 * mid
            diagonals.append(ele)

            if is_prime(ele):
                count += 1

        if ((count / len(diagonals)) * 100) < percent:
            break

        n += 2

    return n


def answer():
    """
    answer().
    """
    return solver(10)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
