"""
    Math 46
"""


def is_prime(number):
    """
    Check primeness of a number.
    """
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def solver():
    """
    Find smallest number which violates GoldBach's
    conjecture.
    """
    number = 2
    prime_list = [2]

    while True:
        flag = 1

        if number % 2 == 0:
            number += 1
            continue

        if is_prime(number):
            prime_list.append(number)
            number += 1
            continue

        idx = len(prime_list) - 1
        val = 0
        while idx >= 0:
            val = ((number - prime_list[idx]) / 2) ** 0.5

            if val == int(val):
                flag = 0
                break

            idx -= 1

        if flag:
            break

        number += 1

    return number


def answer():
    """
    Find the smallest number which violates
    GoldBach's conjecture.
    """
    return solver()


if __name__ == "__main__":
    print(f"answer()={answer()}")
