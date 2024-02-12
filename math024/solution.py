"""
    Module name :- solution
    Method(s) :- factorial(n), remainder_and_count(remainder, n), solver(string, place),
    answer()
"""


def factorial(n):
    """
    Find factorial of n.

    Args:-
        n(int):- An Integer number

    Return
        Factorial of n.
    """
    prod = 1

    for i in range(2, n + 1):
        prod *= i

    return prod


def remainder_and_count(remainder, n):
    """
    Find the bucket in which the last number falls.

    Args:-
        remainder(int):- Integer number to separate
        n(int):- Number whose factorial to subtracted
        from remainder.

    Return
        Remainder and place of bucket.
    """
    fact_n = factorial(n)
    count = 0

    while remainder > fact_n:
        remainder -= fact_n
        count += 1

    return remainder, count


def solver(string, place=0):
    """
    Find the combination of string at given place.

    Args:-
        string(str):- A string whose combination to find.
        place(int):- The place at which combination to find.

    Return:
        Combination of string at given place.
    """

    length = len(string)

    if place > factorial(length):
        return 0

    n = length - 1
    result = ""

    while len(result) < length:
        place, count = remainder_and_count(place, n)

        n -= 1
        result += string[count]
        string = string[:count] + string[count + 1 :]

        if place == 1:
            result += string

    return result


def answer():
    """
    Find combination of '0123456789' at 1e6 place.

    Return
        Combination of '0123456789' at 1e6 place.
    """
    return solver("0123456789", 1e6)


if __name__ == "__main__":
    print(f'solver("012", 3) = {solver("012", 3)}')
    print(f"answer() = {answer()}")
