"""
    Module name :- solution
    Method(s) :- fibonacci(num1, num2), solver(n), answer()
"""


def fibonacci(num1: int, num2: int):
    """
    Generates a fibonacci number one at a time.

    Return
        Fibonacci number.
    """
    len_num1, len_num2 = len(num1), len(num2)
    j = -1
    result = ""
    carry = 0

    while j >= -len_num2:
        a, b = int(num1[j]), int(num2[j])
        result = str((a + b + carry) % 10) + result
        carry = (a + b + carry) // 10
        j -= 1

    if len_num1 > len_num2:
        result = str(int(num1[: len_num1 - len_num2]) + carry) + result
    elif carry:
        result = str(carry) + result

    return result, num1


def solver(n: int):
    """
    Find the index of fibonacci number whose length is n.

    Args:-
        n(int):- Length of fibonacci number.

    Return
        Index of fibonacci number of length n.
    """

    num1, num2 = "1", "1"
    index = 2

    while len(num1) < n:
        num1, num2 = fibonacci(num1, num2)
        index += 1

    return index


def answer():
    """
    Find the index of fibonacci number of length n.

    Return
        Length of fibonacci number of length n.
    """
    return solver(1000)


if __name__ == "__main__":
    print(f"solver(10) = {solver(10)}")
    print(f"answer() = {answer()}")
