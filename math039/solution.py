"""
    Find the value in range upto n which has maximum integral length sides.
"""


def solver(n):
    """
    Finds the value in range upto n which has maximum integral length sides.
    """
    integer_right_triangles = {}

    for number in range(12, n + 1):
        for a in range(1, number // 3):
            b = (number**2 - 2 * number * a) // (2 * (number - a))
            c = number - a - b

            if a**2 + b**2 == c**2:
                integer_right_triangles[number] = integer_right_triangles.get(
                    number, []
                ) + [(a, b, c)]

    return sorted(
        integer_right_triangles.items(), key=lambda x: len(x[1]), reverse=True
    )[0][0]


def answer():
    """
    Find the value in range upto 1000 which has maximum integral length sides.
    """
    return solver(1000)


if __name__ == "__main__":
    print(f"answer={answer()}")
