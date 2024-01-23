"""
    Find the sum of all numbers whose sum of nthh power
    of its digit equals to the number.
"""


def find_digit_power_sum(number, n):
    """
    Find sum of power of digits.
    """
    return sum(find_digit_power(int(num), n) for num in str(number))


def find_digit_power(num, n):
    """
    Find value of power of digit.
    """
    if n == 1:
        return num

    product = str(num)
    for _ in range(n - 1):
        product_reverse = product[::-1]
        carry = 0
        product = ""

        for digit in product_reverse:
            value = int(digit) * num + carry
            product = str(value % 10) + product
            carry = value // 10

        if carry:
            product = str(carry) + product

    return int(product)


def solver(n):
    """
    Find the sum of all numbers whose sum of nth power
    of its digit equals to the number.
    """
    return sum(
        num for num in range(10, 10000000) if num == find_digit_power_sum(num, n)
    )


def answer():
    """
    Find the sum of all numbers whose sum of 5th power
    of its digit equals to the number.
    """
    return solver(5)


if __name__ == "__main__":
    print(f"solver(4) = {solver(4)}")
    print(f"answer() = {answer()}")
