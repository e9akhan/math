"""
    Math 56
"""

def power(a, b):
    """
    Find powers.
    """
    prod = str(a)

    for _ in range(b - 1):
        prod_rev = prod[::-1]
        prod = ""
        carry = 0

        for digit in prod_rev:
            val = int(digit) * a + carry
            carry = val // 10
            prod = str(val % 10) + prod

        if carry:
            prod = str(carry) + prod

    return prod


def solver(n):
    """
    Find prod having maximum sum of its digit of powers from 1, n.
    """
    summation = []
    for a in range(1, n):
        for b in range(1, n):
            result = power(a, b)

            summation.append(sum(int(digit) for digit in result))

    return sorted(summation, reverse=True)[0]


def answer():
    """
    Find prod having maximum sum of its digit of powers from 1, 99.
    """
    return solver(100)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
