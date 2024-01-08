"""
    Module name :- solution
    Method(s) :- find_collatz(start, end), solver(p: int = None, q: int = None),
    answer()
"""


def find_collatz(start, end):
    """
    Find the collatz of the given number.

    Args:-
        start(int) :- Starting point of the range.
        end(int) :- Ending point of the range.

    Return
        The count of collatz sequence of the number.
    """

    collatz = {1: 1}

    for value in range(start, end + 1):
        number = value
        count = 0

        while number >= 1:
            if number in collatz:
                count += collatz[number]
                break
            elif number % 2 == 0:
                number //= 2
                count += 1
            else:
                number = 3 * number + 1
                count += 1

        collatz[value] = count

    return collatz


def solver(p: int = None, q: int = None):
    """
    Find the first number having maximum collatz sequence over the range.

    Args:-
        p(int) :- Starting point of the range.
        q(int) :- Ending point of the range.

    Return
        Smallest number having maximum collatz sequence over the range.
    """

    if not (p or q):
        return None

    start = 1
    end = p or q

    if p and q:
        start = p
        end = q

    collatz = find_collatz(start, end)
    resultant = {}

    for key, value in collatz.items():
        if value in resultant:
            resultant[value] += [key]
        else:
            resultant[value] = [key]

    return resultant[sorted(resultant)[-1]][0]


def answer():
    """
    Find the smallest number having maximum collatz sequence over 1000000.

    Return
        Smallest number having maximum collatz sequence over 1000000.
    """
    return solver(1000000)


if __name__ == "__main__":
    print(f"solver(22) = {solver(22)}")
    print(f"answer() = {answer()}")
