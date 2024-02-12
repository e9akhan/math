"""
    Module name :- solution
    Method(s) :- is_abundant(num), solver(n, p, q), answer()
"""


def is_abundant(num):
    """
    Check whether the given num is abundant number
    or not.

    Args:-
        num(int) :- Number
    """
    factor_sum = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            factor_sum += i

    return factor_sum > num


def solver(p: int, q: int = None):
    """
    Find the sum of all positive integers which cannot be
    written as the sum of n abundant numbers where all the
    abundant numbers lie within the range p and q.

    Args:-
        n(int):- Numbers of abundant numbers to sum.
        p(int) :- Starting or ending point of range.
        q(int) :- Ending point of range.

    Return
        Sum of all positive integers which cannot be
        written as the sum of n abundant numbers where all the
        abundant numbers lie within the range p and q.
    """
    start, end = 1, p or q

    if p and q:
        start, end = p, q

    if start > end:
        return 0

    numbers = list(range(start, end + 1))
    abundant_numbers = [num for num in numbers if is_abundant(num)]
    sum_n_abundant_numbers = [
        abundant_numbers[i] + abundant_numbers[j]
        for i in range(len(abundant_numbers))
        for j in range(i, len(abundant_numbers))
    ]

    return sum(set(numbers) - set(sum_n_abundant_numbers))


def answer():
    """
    Find the sum of all positive integers which cannot be
    written as the sum of 2 abundant numbers.

    Return
        Sum of all positive integers which cannot be
        written as the sum of 2 abundant numbers.
    """
    return solver(1, 28123)


if __name__ == "__main__":
    print(f"answer()={answer()}")
