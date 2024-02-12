"""
    Math 49
"""


def is_prime(num):
    """
    Check primeness of a number.
    """
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def permutations(num, index, perm_list):
    """
    Find permutations.
    """
    if index == len(num) - 1:
        perm_list.append(int("".join(num)))
        return perm_list

    for i in range(len(num)):
        num_list = list(num)
        num_list[i], num_list[index] = num_list[index], num_list[i]
        perm_list = permutations(num_list, index + 1, perm_list)

    return perm_list


def answer():
    """
    answer().
    """
    primes = [
        number for number in range(1000, 10000) if is_prime(number) and number != 1487
    ]
    num_str = ""

    for prime in primes:
        if prime > 3500:
            break

        perm_list = permutations(str(prime), 0, [])

        mid = prime + 3330
        large = mid + 3330

        if (
            mid in primes
            and large in primes
            and mid in perm_list
            and large in perm_list
        ):
            num_str = str(prime) + str(mid) + str(large)
            break

    return num_str


if __name__ == "__main__":
    print(f"answer()={answer()}")
