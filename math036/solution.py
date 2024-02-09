"""
    Find the sum of all numbers, less than one million,
    which are palindromic in base and base .
"""


def find_binary(number):
    """
    Find binary of a given number.
    """
    binary = ""

    while number > 0:
        binary += str(number % 2)
        number //= 2

    return binary


def palindrome(number):
    """
    Check for palindrome.
    """
    return number == number[::-1]


def solver(end_range):
    """
    Find the sum of all numbers, less than end_range,
    which are palindromic in base and base .
    """
    total = 0

    for i in range(1, end_range):
        if not palindrome(str(i)):
            continue

        binary = find_binary(i)

        j = 0
        while binary[j] == 0:
            binary = binary[1:]
            j += 1

        if palindrome(binary):
            total += i

    return total


def answer():
    """
    Find the sum of all numbers, less than one million,
    which are palindromic in base and base .
    """
    return solver(int(1e6))


if __name__ == "__main__":
    print(f"answer() = {answer()}")
