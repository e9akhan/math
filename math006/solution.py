"""
    Module Name :- solution
    Method(s) :- solver(start, end), answer()
"""


def solver(start, end):
    """
    Find the sum of square of numbers and square of sum of numbers
    over a range

    Args:
        start(int) :- Starting point of range.
        end(int) :- Ending point of range.

    Return:
        Absolute difference of sum of square of numbers and square of sum of
        numbers.
    """
    if start > end:
        return -1

    squares_sum = 0

    for i in range(start, end + 1):
        squares_sum += i**2

    sums_square = ((end * (end + 1) / 2) - (start * (start - 1) / 2)) ** 2

    diff = sums_square - squares_sum
    return int(abs(diff))


def answer():
    """
    Find the difference of sum of squares of number and squares of sum
    of numbers between 1-100
    """
    return solver(1, 100)


if __name__ == "__main__":
    print(f"solver(1, 10) = {solver(1, 10)}")
    print(f"answer() = {answer()}")
