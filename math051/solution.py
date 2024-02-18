"""
    Math 51
"""


def is_prime(num):
    """
    Check whether number is prime or not.
    """
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(start, end):
    """
    Generate primes.
    """
    return [num for num in range(start, end + 1) if is_prime(num)]


def replace_digits(number, digit, positions):
    """
    Replace digits.
    """
    numbers = []
    number = str(number)

    for i in range(digit, 10):
        num_list = list(number)
        for idx in positions:
            num_list[idx] = str(i)
        numbers.append(int("".join(num_list)))

    return numbers


def count_primes(number, digit, positions, prime_list):
    """
    Count primes.
    """
    numbers = [number] + replace_digits(number, digit + 1, positions)
    return len([num for num in numbers if num in prime_list])


def solver(n):
    """
    solver(n).
    """
    prime_list = generate_primes(11, 1000000)

    for prime in prime_list:
        for digit in range(10):
            prime_str, digit_str = str(prime), str(digit)
            if digit_str in prime_str[:-1]:
                positions = [
                    idx for idx, char in enumerate(prime_str[:-1]) if char == digit_str
                ]
                prime_count_size = count_primes(prime, digit, positions, prime_list)
                if prime_count_size >= n:
                    return prime

    return 0


def answer():
    """
    answer().
    """
    return solver(8)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
