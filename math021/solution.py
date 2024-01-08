"""
    Module name :- solution
    Method(s) :- solver(a, b), answer()
"""


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

    amicable_numbers = []

    for number in range(start, end + 1):
        if number in amicable_numbers:
            continue

        sum1 = 1
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                sum1 += i
                sum1 += number // i

        if sum1 < number:
            continue

        sum2 = 1
        for j in range(2, int(sum1**0.5) + 1):
            if sum1 % j == 0:
                sum2 += j
                sum2 += sum1 // j

        if sum2 == number and sum1 != number:
            amicable_numbers += [number, sum1]

    return sum(amicable_numbers)


def answer():
    """
    Find sum of amicable numbers under 10000.

    Return
        Sum of amicable numbers under 10000.
    """
    return solver(10000)


if __name__ == "__main__":
    print(f"solver(100) = {solver(100)}")
    print(f"answer() = {answer()}")
