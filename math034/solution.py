"""
    Find the sum of number whose sum of factorial of its
    digit is equal to number.
"""


def find_factorial(num):
    """
    Find factorial of num.
    """
    product = "1"
    for i in range(2, num + 1):
        product_reverse = product[::-1]
        carry = 0
        product = ""

        for digit in product_reverse:
            value = int(digit) * i + carry
            product = str(value % 10) + product
            carry = value // 10

        if carry:
            product = str(carry) + product

    return int(product)


def solver(a: int = None, b: int = None):
    """
    Find the sum of number whose sum of factorial of its
    digit is equal to number.
    """
    summation = 0

    start, end = 10, a or b

    if a and b:
        start, end = a, b

    for number in range(start, end + 1):
        factorial_summation = sum(find_factorial(int(num)) for num in str(number))

        if number == factorial_summation:
            summation += factorial_summation

    return summation


def answer():
    """
    Find the sum of number whose sum of factorial of its
    digit is equal to number upto 10000000.
    """
    return solver(10000000)


if __name__ == "__main__":
    print(f"solver(145, 145) = {solver(145, 145)}")
    print(f"answer() = {answer()}")
