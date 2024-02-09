"""
    Find circular prime numbers from a to b.
"""


def is_prime(num):
    """
    Check primeness of number.
    """
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def solver(a: int = None, b: int = None):
    """
    Find circular prime numbers from a to b.
    """
    start, end = 2, a or b

    if a and b:
        start, end = a, b

    count = 0

    for num in range(start, end + 1):
        num_str = str(num)

        for _ in range(len(num_str)):
            if not is_prime(int(num_str)):
                break
            num_str = num_str[1:] + num_str[0]
        else:
            count += 1

    return count


def answer():
    """
    Find circular prime numbers upto 10000000.
    """
    return solver(10000000)


if __name__ == "__main__":
    print(f"solver(197, 197) = {solver(197, 197)}")
    print(f"answer() = {answer()}")
