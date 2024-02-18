"""
    Math 75
"""


def solver(n):
    """
    solver().
    """
    start = 12
    int_right_triangle_dict = {}

    for p in range(start, n + 1):
        for a in range(1, p // 3):
            b = (p * p - 2 * a * p) // (2 * (p - a))
            c = p - a - b

            if a**2 + b**2 == c**2:
                int_right_triangle_dict[p] = int_right_triangle_dict.get(p, []) + [
                    (a, b, c)
                ]

                if len(int_right_triangle_dict[p]) > 1:
                    break

    return len([p for p, lst in int_right_triangle_dict.items() if len(lst) == 1])


def answer():
    """
    answer().
    """
    return solver(1500000)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
