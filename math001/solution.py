"""
    Module Name :- solution
    method(s) :- answer(), solver(factors, start, end)
"""


def answer():
    """
    This code works specifically for finding sum of multiples of 1 or a pair of number/s.
    """
    return solver([3, 5], 1, 1000)


def solver(factors, start, end):
    """
    The code accepts a range of number and finds the sum of multiple of the numbers given in the
    list over the net range.

    Args:
    start: int - Accepts the starting point of range.
    end: int - Accepts the ending point of range.
    factors:list - Accept a list of numbers whose multiple has to find.

    Return:
    returns an integer sum else -1
    """
    factor_list = set()

    for elements in factors:
        start_ = (start // elements) * elements
        for j in range(start_ + elements, end, elements):
            factor_list.add(j)

    if factor_list:
        return sum(factor_list)
    return -1


if __name__ == "__main__":
    print(
        f"solver([2, 3, 5, 7, 11], 34567, 1234567) = {solver([2, 3, 5, 7, 11], 34567, 1234567)}"
    )
