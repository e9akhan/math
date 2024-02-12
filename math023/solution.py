"""
    Module name :- solution
    Method(s) :- is_abundant(num), solver(n, p, q),
    find_sum_n_abundant_numbers(
        abundant_numbers,
        n, n_abundant_sum=0,
        n_abundant_sum_list=[]
    ), answer()
"""


def is_abundant(num):
    """
    Check whether the given num is abundant number
    or not.

    Args:-
        num(int) :- Number
    """
    factor_sum = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            factor_sum += i
            factor_sum += num // i

    return factor_sum > num


def find_sum_n_abundant_numbers(
    abundant_numbers,
    n,
    n_abundant_sum_list,
    n_abundant_sum=0,
):
    """
    Find the n abundant_numbers in given list.

    Args:-
        abundant_numbers(list) :- List of abundant numbers.
        n(int) :-  Number of abundant numbers to sum.

    Return
        List containing sum of combinations of n abundant
        numbers of given list.
    """
    if n == 0:
        n_abundant_sum_list.append(n_abundant_sum)
        return n_abundant_sum_list

    for num in abundant_numbers:
        n_abundant_sum_list = find_sum_n_abundant_numbers(
            abundant_numbers, n - 1, n_abundant_sum_list, n_abundant_sum + num
        )

    return n_abundant_sum_list


def solver(n: int, p: int, q: int = None):
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
    sum_n_abundant_numbers = set(find_sum_n_abundant_numbers(abundant_numbers, n, []))

    return sum(set(numbers) - sum_n_abundant_numbers)


def answer():
    """
    Find the sum of all positive integers which cannot be
    written as the sum of 2 abundant numbers.

    Return
        Sum of all positive integers which cannot be
        written as the sum of 2 abundant numbers.
    """
    return solver(2, 28123)


if __name__ == "__main__":
    print(f"answer()={answer()}")
