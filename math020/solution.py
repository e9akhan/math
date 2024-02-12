"""
    Module name :- solution
    Method(s) :- solver(n), answer()
"""


def solver(n):
    """
    Finds factorial of n.

    Args:-
        n(int) :- An integer number.

    Return
        Factorial of n.
    """
    product = "1"

    for i in range(2, n + 1):
        carry = 0
        product_reverse_copy = product[::-1]
        product = ""

        for digit in product_reverse_copy:
            prod = carry + int(digit) * i
            product = str(prod % 10) + product
            carry = prod // 10

        if carry:
            product = str(carry) + product

    return sum(int(digit) for digit in product)


def answer():
    """
    Finds factorial of n.

    Args:-
        n(int) :- An integer number.

    Return
        Factorial of n.
    """
    return solver(100)


if __name__ == "__main__":
    print(f"solver(10) = {solver(10)}")
    print(f"answer() = {answer()}")
