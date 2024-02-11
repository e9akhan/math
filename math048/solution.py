"""
    Find the last ten digits of sum of self powers
    upto n.
"""


def find_powers(num):
    """
    Find self power.
    """
    prod = str(num)
    for _ in range(num - 1):
        reverse_prod = prod[::-1]
        carry = 0
        prod = ""

        for digit in reverse_prod:
            val = int(digit) * num + carry
            prod = str(val % 10) + prod
            carry = val // 10

        if carry:
            prod = str(carry) + prod

    return prod


def add(num1, num2):
    """
    Add two numbers.
    """
    addition = ""
    carry = 0

    num1_rev, num2_rev = num1[::-1], num2[::-1]

    for i in range(len(num2)):
        val = int(num1_rev[i]) + int(num2_rev[i]) + carry
        addition = str(val % 10) + addition
        carry = val // 10

    remaining = num1[: len(num1) - i - 1]

    if remaining:
        carry += int(remaining)

    addition = str(carry) + addition if carry else addition

    return addition


def solver(n):
    """
    Find last ten digit of sum of sl=elf power upto
    n.
    """
    total = "0"
    for num in range(1, n + 1):
        total = add(find_powers(num), total)
    return total[-10:]


def answer():
    """
    Find last ten digit of sum of self powers
    upto 1000.
    """
    return solver(1000)


if __name__ == "__main__":
    print(f"answer()={answer()}")
