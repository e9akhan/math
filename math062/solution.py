"""
    Module name :- Math 62
"""


def find_permutations(number, idx, permutation_list):
    """
    Find permutations.
    """
    if idx == len(number) - 1:
        num = int("".join(number))

        if len(str(num)) == len(number):
            permutation_list.add(num)
        return permutation_list

    for i in range(idx, len(number)):
        num_list = list(number)
        num_list[idx], num_list[i] = num_list[i], num_list[idx]
        permutation_list = find_permutations(num_list, idx + 1, permutation_list)

    return permutation_list


def solver(n):
    """
    solver(n).
    """
    all_permutations = []
    number = 1
    while True:
        cube = number**3
        print(number)

        if cube in all_permutations:
            number += 1
            continue

        permutations = list(find_permutations(str(cube), 0, set()))

        count = 0
        for permutation in permutations:
            val = round(permutation ** (1 / 3), 12)
            if val == int(val):
                count += 1

        if count == n:
            break

        all_permutations += permutations
        number += 1

    return cube


def answer():
    """
    answer().
    """
    return solver(5)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
