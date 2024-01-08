"""
    Module name :- solution
    Method(s) :- backtrack(matrix, x, y), solver(num), answer()
"""


NUM = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 
"""


def answer():
    """
    Find the maximum sum in NUM.

    Return
        Maximum sum in NUM
    """
    return solver(NUM)


def backtrack(matrix, x, y):
    """
    Find the sum of number at current node and next node.

    Args:
        matrix(list) :- Matrix storing number
        x(int) :- Vertical position of node.
        y(int) :- Horizontal poistion of node.

    Return:
        Sum of number at current node and next node.
    """
    if x == len(matrix) - 1:
        return int(matrix[x][y])

    return int(matrix[x][y]) + max(
        backtrack(matrix, x + 1, y), backtrack(matrix, x + 1, y + 1)
    )


def solver(num):
    """
    Find the maximum sum of number in given matrix.

    Args:
        num(str) :- String of numbers

    Return:
        Maximum sum of number in given matrix.
    """
    matrix = []

    for ls in num.split("\n")[1:]:
        matrix.append(ls.split(" "))

    matrix = matrix[:-1]

    return backtrack(matrix, 0, 0)


if __name__ == "__main__":
    NUM = """
3
7 4
2 4 6
8 5 9 3
"""

    print(f"solver(NUM) = {solver(NUM)}")
    print(f"answer() = {answer()}")
