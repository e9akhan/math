"""
    Module name :- solution
    Method(s) :- recurrence_part(number), solver(p, num),
    find_recurrence_number(number_recurrence, num), answer()
"""


def recurrence_part(number):
    """
    Find the recurrence number of decimal part.

    Args:-
        number :- Number from which to divide

    Return
        Recurrence number.
    """
    length = len(str(number))
    numerator = 10 ** (length)

    quotient = ""
    numerator_list = [0]

    while numerator not in numerator_list:
        numerator_list.append(numerator)
        numerator = numerator % number * 10
        quotient += str(numerator // number)

    n = numerator_list.index(numerator)

    if numerator == 0:
        return quotient
    return quotient[n - 1 :]


def find_recurrence_number(number_recurrence, num):
    """
    Find the number which has num in recurrence part.

    Args:-
        number_recurrence(dict):- Number and their recurrence.
        num(list):- The num which has to be in recurrence.

    Return
        Number which has num in recurrence part.
    """

    num = "".join(sorted(str(num[0])))

    for number, recurrence in number_recurrence.items():
        if num in "".join(sorted(recurrence)):
            return number

    return 0


def solver(p: int, num: list = None):
    """
    Find the number has the longest recurrence or num.

    Args:
        p(int):- Ending range.
        num(list):- The num which has to be in recurrence.

    Return
        Number has the longest recurrence or num.
    """
    number_recurrence = {i: recurrence_part(i) for i in range(1, p)}

    if num:
        return find_recurrence_number(number_recurrence, num)
    return sorted(
        number_recurrence,
        key=lambda recur: len(number_recurrence.get(recur)),
        reverse=True,
    )[0]


def answer():
    """
    Find the number which has longest recurrence under 1000.

    Return:-
        Number which has longest recurrence under 1000.
    """
    return solver(1000)


if __name__ == "__main__":
    print(f'solver(10, ["124578"]) = {solver(10, ["124578"])}')
    print(f"answer() = {answer()}")
