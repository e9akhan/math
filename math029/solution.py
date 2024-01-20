"""
    Find the number of distict power with a^b.
"""


def find_powers(number, power):
    """
    Find the value of number ^ power.
    """
    product = str(number)

    for _ in range(power - 1):
        carry = 0
        product_reverse = product[::-1]
        product = ""

        for digit in product_reverse:
            value = int(digit) * number + carry

            product = str(value % 10) + product
            carry = value // 10

        if carry:
            product = str(carry) + product

    return product


def solver(a, b):
    """
    Find the number of distict power with number^power.
    """
    return len(
        set(
            find_powers(number, power)
            for power in range(a, b + 1)
            for number in range(a, b + 1)
        )
    )


def answer():
    """
    Find the number of distict power with number^power
    where 2<=number<=100 and 2<=power<=100.
    """
    return solver(2, 100)


if __name__ == "__main__":
    print(f"solver(2, 5) = {solver(2, 5)}")
    print(f"answer() = {answer()}")
