"""
    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a through pandigital.
"""


def answer():
    """
    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a through pandigital.
    """
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    prod_set = set()
    track = 1
    second_end_range = 10000

    for num1 in range(1, 1001):
        if (num1 ** (1 / track)) == 10:
            second_end_range //= 10
            track += 1

        for num2 in range(num1 + 1, second_end_range):
            prod = num1 * num2

            num_str = str(num1) + str(num2) + str(prod)

            if len(set(num_str)) != len(num_str):
                continue

            if numbers == sorted(num_str):
                prod_set.add(prod)
    return sum(prod_set)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
