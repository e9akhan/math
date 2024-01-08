"""
    Module name :- solution
    Method(s) :- solver(m, n), answer()
"""


def solver(m, n):
    """
    Find the number of ways to move to the end point from start.

    Args:-
        m(int) :- Height of grid
        n(int) :- Width of grid

    Return
        Number of ways to reach endpoint from start.
    """
    row = [1] * (n + 1)

    for _ in range(m):
        new_row = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            new_row[i] = row[i] + new_row[i + 1]
        row = new_row

    return row[0]


def answer():
    """
    Find the number of posiible ways to reach endpoint from start in 20x20 grid.

    Return:
        Number of possible ways to reach end from start in 20x20 grid.
    """
    return solver(20, 20)


if __name__ == "__main__":
    print(f"solver(3, 3) = {solver(3, 3)}")
