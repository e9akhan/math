"""
    Math 052
"""


def solver(n):
    """
    All number uptill n multiples having same digit.
    """

    flag = 0
    number = 1

    while not flag:
        sort_num = sorted(str(number))
        for i in range(2, n + 1):
            val = str(i * number)

            if sorted(val) != sort_num:
                break
        else:
            flag = 1

        number += 1

    return number - 1


def answer():
    """
    All number uptill 6 multiples having same digit.
    """
    return solver(6)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
