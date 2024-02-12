"""
    Find next triangle number that is also pentagonal
    and hexagonal.
"""


def solver():
    """
    solver()
    """
    pen_num_list = [(i * (3 * i - 1) // 2) for i in range(166, 100000)]

    hex_num = 0
    for i in range(144, 100000):
        hex_num = i * (2 * i - 1)

        if hex_num in pen_num_list:
            break

    return hex_num


def answer():
    """
    Find next triangle number that is
    hexagonal and pentagonal.
    """
    return solver()


if __name__ == "__main__":
    print(f"answer()={answer()}")
