"""
    Module name :- solution
    Method(s) :- solver(a, b), answer(), factor_sum(nm)
"""


def factor_sum(num):
    """
    Find sum of factors.

    Args:-
        num(int):- Number.

    Return
        Sum of factors of given number.
    """
    sum1 = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum1 += i
            sum1 += num // i

    return sum1


def solver(a: int, b: int = None):
    """
    Find sum of amicable numbers from a to b.

    Args:-
        a(int) :- Starting point of range.
        b(int) :- ending point of range.

    Return
        Sum of amicable numbers.
    """
    start = 12
    end = a or b

    if a and b:
        start = a
        end = b

    if start > end:
        return 0

    number_and_factor_sum = {}

    for number in range(start, end + 1):
        sum_factors = factor_sum(number)
        if sum_factors not in (1, number):
            number_and_factor_sum.update({number: sum_factors})

    amicable_numbers = [
        key
        for key, value in number_and_factor_sum.items()
        if value in number_and_factor_sum and number_and_factor_sum[value] == key
    ]

    return sum(amicable_numbers)


def answer():
    """
    Find sum of amicable numbers under 10000.

    Return
        Sum of amicable numbers under 10000.
    """
    return solver(10000)


if __name__ == "__main__":
    print(f"solver(300) = {solver(300)}")
    print(f"answer() = {answer()}")
