"""
    Find max n digit pandigital prime number
"""


def is_prime(number):
    """
    Check whether number is prime or not.
    """
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def combinations(num_str, index, combination_list):
    """
    Find combinatio of num_str
    """
    if index == len(num_str) - 1:
        combination_list.append("".join(num_str))

    for j in range(index, len(num_str)):
        num_str_list = list(num_str)
        num_str_list[index], num_str_list[j] = num_str_list[j], num_str_list[index]

        combination_list = combinations(num_str_list, index + 1, combination_list)

    return combination_list


def solver(n):
    """
    Find max pandigital prime number.
    """
    max_pandigital_prime = 0
    for i in range(1, n + 1):
        pandigital = [str(j) for j in range(1, i + 1)]
        combination_list = sorted(combinations(pandigital, 0, []))

        for combination in combination_list:
            number = int(combination)

            if is_prime(number):
                max_pandigital_prime = number

    return max_pandigital_prime


def answer():
    """
    Find max pandigital prime number upto n digit.
    """
    return solver(9)


if __name__ == "__main__":
    print(f"answer()={answer()}")
