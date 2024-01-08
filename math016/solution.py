"""
    Module name :- solution
    Method(s) :- solver(n), answer()
"""


def solver(n):
    """
    Find the sum of digit of 2^n.

    Args:-
        n(int) :- Power of 2.

    Return
        Sum of digits of 2^n.
    """
    product = "1"
    total = 0

    for _ in range(1, n + 1):
        carry = 0
        val2 = 0
        product_copy = product[::-1]
        product = ""
        for digit in product_copy:
            val = carry + int(digit) * 2
            val2 = val % 10
            carry = val // 10

            product = str(val2) + product

        if carry:
            product = str(carry) + product

    for digit in product:
        total += int(digit)

    return total


def answer():
    """
    Find the sum of digit of 2^1000.

    Return
        Sum of digits of 2^1000.
    """
    return solver(1000)


if __name__ == "__main__":
    print(f"solver(15) = {solver(15)}")
