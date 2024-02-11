"""
    Math 43
"""


def combinations(num_str, index, combination_list):
    """
    Find combination of given num_str.
    """
    if index == len(num_str) - 1:
        combination_list.append("".join(num_str))

    for i in range(index, len(num_str)):
        num_list = list(num_str)
        num_list[index], num_list[i] = num_list[i], num_list[index]

        combination_list = combinations(num_list, index + 1, combination_list)

    return combination_list


def solver(n):
    """
    solver().
    """
    pandigital = [str(i) for i in range(n)]

    temp_list = combinations(pandigital, 0, [])
    combination_list = [number for number in temp_list if not number.startswith("0")]
    sub_str_div = []
    prime_list = [2, 3, 5, 7, 11, 13, 17]

    for number in combination_list:
        for i in range(1, n - 2):
            sub_str = int(number[i : i + 3])
            if (sub_str % prime_list[i - 1]) != 0:
                break
        else:
            sub_str_div.append(int(number))

    return sum(sub_str_div)


def answer():
    """
    answer().
    """
    return solver(10)


if __name__ == "__main__":
    print(f"answer()={answer()}")
