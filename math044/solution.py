"""
    Math 25.
"""


def solver():
    """
    Solver Mtd.
    """
    pentagonal_number_list = []
    pent_dict = {}
    for i in range(1, 2400):
        pentagonal_number = i * (3 * i - 1) // 2
        pentagonal_number_list.append(pentagonal_number)

        j = 0

        while (pentagonal_number - pentagonal_number_list[j]) > (
            pentagonal_number // 2
        ):
            num1 = pentagonal_number_list[j]
            num2 = pentagonal_number - num1

            if not num2 in pentagonal_number_list:
                j += 1
                continue

            add = num1 + num2
            diff = num2 - num1

            if add in pentagonal_number_list and diff in pentagonal_number_list:
                pent_dict[(num1, num2)] = diff

            j += 1

    key = sorted(pent_dict.items(), key=lambda x: x[1])[0][0]

    return pent_dict[key]


def answer():
    """
    Answer mtd.
    """
    return solver()


if __name__ == "__main__":
    print(f"answer()={answer()}")
