"""
    Module name :- solution
    method(s) :- answer(), fibonacci(), fibonacci_sum(end, task),
    solver(start, end, even, odd)
"""


def fibonacci():
    """
    Generator for generating fibonacci series.

    Return:
        a(int) :- Returns a fibonacci number.
    """
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def fibonacci_sum(end, task):
    """
    Find the sum of the even/odd fibonacci numbers upto end.

    Args:
        end(int) :- The number upto which the fibonacci series must be generated.
        task(str) :- It accepts string value(here even/odd).

    Return:
        total(int) :- Sum of even/odd fibonacci number upto end.
    """
    total = 0
    fibonacci_ = fibonacci()
    fib = next(fibonacci_)
    remainder = 0

    if task == "odd":
        remainder = 1

    while fib < end:
        if fib % 2 == remainder:
            total += fib
        fib = next(fibonacci_)

    return total


def solver(start, end, even=False, odd=False):
    """
    Find the sum of even/odd fibonacci number over a range.

    Args:-
        start(int) :- Starting point of the range.
        end(int) :- Ending point of the range.
        even(bool) :- Must be True if sum of even fibonacci numbers to be calculated.
        odd(bool) :- Must be True if sum of odd fibonacci numbers to be calculated.
    """
    avg_sum = 0

    if end < start:
        return -1

    if even:
        end_sum = fibonacci_sum(end, "even")
        start_sum = fibonacci_sum(start, "even")
        avg_sum += end_sum - start_sum

    if odd:
        end_sum = fibonacci_sum(end, "odd")
        start_sum = fibonacci_sum(start, "odd")
        avg_sum += end_sum - start_sum

    return avg_sum


def answer():
    """
    Find the sum of even fibonacci numbers upto 4000000

    Return:
        Sum of even fibonacci numbers upto 4000000
    """
    return solver(0, 4 * 10**6, even=True)


if __name__ == "__main__":
    print(
        f"""solver(start=15812, end=91581312, even=False, odd=True) = {solver(
            start=15812, end=91581312, even=False, odd=True
        )}"""
    )
