"""
    Module name :- solution
    Method(s) :- find_number_of_factors(number), solver(n),
    answer()
"""


def find_number_of_factors(number):
    """
    Number of factors of given number.

    Args:-
        number(int) :- An integer number

    Return:-
        Number of factors of given number
    """
    count = 0

    if number < 2:
        return 1

    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            count += 2

    if int(number**0.5) ** 2 == number:
        count -= 1

    return count


def solver(n):
    """
    Find the number having more than n divisors.

    Args:-
        n(int) :- Number of divisors.

    Return
        Number having more than n divisors.
    """
    if n <= 0:
        return -1

    number = 1
    count = 1
    while True:
        count += 1
        if find_number_of_factors(number) > n:
            return number
        number += count


def answer():
    """
    Find number having more than 500 divisors.

    Return
        Number having more than 500 divisors.
    """
    return solver(500)


if __name__ == "__main__":
    print(f"solver(5) = {solver(5)}")
    print(f"answer() = {answer()}")
