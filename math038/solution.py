"""
    What is the largest 1 to 9 pandigital 9-digit number that can
    be formed as the concatenated product of an integer with (1,2,..n) where n>1?
"""


def solver(n):
    """
    What is the largest 1 to n pandigital 9-digit number that can
    be formed as the concatenated product of an integer with (1,2,..n) where n>1?
    """
    pandigital = [str(i) for i in range(1, n + 1)]

    number = 1
    max_num_length = n // 2
    max_pandigital = 0

    while len(str(number)) <= max_num_length:
        concat_str = ""
        i = 1
        while len(concat_str) <= n:
            concat_str += str(number * i)
            i += 1

            if sorted(concat_str) == pandigital:
                max_pandigital = int(concat_str)

        number += 1

    return max_pandigital


def answer():
    """
    What is the largest 1 to 9 pandigital 9-digit number that can
    be formed as the concatenated product of an integer with (1,2,..n) where n>1?
    """
    return solver(9)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
