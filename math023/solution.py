"""
    Module name :- solution
    Method(s) :- get_factor_sum(number), solver(p, q), answer()
"""


def get_factor_sum(number: int):
    """
    Find the sum of factors of given number.

    Args:-
        number(int):- Number.

    Return
        Sum of factors of given number.
    """
    factor_sum = 1

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            factor_sum += i
            factor_sum += number // i

    return factor_sum


def solver(p: int, q: int = None):
    """
    Find the sum of all non-abundant numbers.

    Args:-
        p(int) :- Starting or ending point of range.
        q(int) :- Ending point of range.

    Return
        Sum of all non-abundant numbers over given range.
    """
    start = 1
    end = p or q

    if p and q:
        start = p
        end = q

    if start > end:
        return 0

    abundant_numbers = [number for number in range()]
    all_numbers = list(range(start, end + 1))

    for number in :

        if number < get_factor_sum(number):
            abundant_numbers.append(number)

    non_abundant_numbers = [number for number in range(start, end+1) if number not in abundant_numbers]

    sum_non_abundant_numbers = [i+j for i in non_abundant_numbers for j in non_abundant_numbers]

    return sum(sum_non_abundant_numbers)


def answer():
    """
    Find the sum of all non-abundant numbers.

    Return
        Sum of all non-abundant numbers.
    """
    return solver(28123)


if __name__ == "__main__":
    print(f"solver(1, 1000) = {solver(1, 1000)}")
    print(f"answer() = {answer()}")
