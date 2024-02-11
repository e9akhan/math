"""
    Find next triangle number that is also pentagonal
    and hexagonal.
"""


def solver():
    """
    solver()
    """
    num1, num2, num3 = 286, 166, 144
    tri_num = 40755
    pent_num_list = hex_num_list = []

    while not (tri_num in pent_num_list and tri_num in hex_num_list):
        tri_num = num1 * (num1 + 1) // 2
        pent_num = num2 * (3 * num2 - 1) // 2
        hex_num = num3 * (2 * num3 - 1)

        pent_num_list.append(pent_num)
        hex_num_list.append(hex_num)

        num1 += 1
        num2 += 1
        num3 += 1

    return tri_num


def answer():
    """
    Find next triangle number that is
    hexagonal and pentagonal.
    """
    return solver()


if __name__ == "__main__":
    print(f"answer()={answer()}")
