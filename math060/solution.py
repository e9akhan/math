"""
    Math 60
"""


from itertools import combinations


def is_prime(num):
    """
        Check whether number is prime or not.
    """
    num = int(num)
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def is_concatenated_prime(num1, num2):
    """
        Is concatenated string prime or not.
    """
    concat1 = is_prime(str(num1) + str(num2))
    concat2 = is_prime(str(num2) + str(num1))

    return concat1 and concat2


def solver(n):
    """
        solver().
    """
    prime_list = [num for num in range(2, 1000) if is_prime(num)]
    n_prime_combinations = []

    for combination in combinations(prime_list, n):
        all_prime = 1
        for num1, num2 in combinations(combination, 2):
            if not is_concatenated_prime(num1, num2):
                all_prime = 0
                break

        if all_prime:
            n_prime_combinations = combination
            break

    return sum(n_prime_combinations) if n_prime_combinations else 0


def answer():
    """
        answer().
    """
    return solver(4)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
