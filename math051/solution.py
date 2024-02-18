def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]


def replace_digits(number, digit, positions):
    num_list = list(str(number))
    for idx in positions:
        num_list[idx] = str(digit)

    return int("".join(num_list))


def find_total_primes(num, digit, positions, prime_list):
    count = 1

    for i in range(digit + 1, 10):
        replaced_num = replace_digits(num, i, positions)
        if replaced_num in prime_list:
            count += 1
    return count


def solver(n):
    prime_list = generate_primes(11, 1000000)

    for prime in prime_list:
        for digit in range(10):
            prime_str, digit_str = str(prime), str(digit)
            positions = [
                idx for idx, char in enumerate(prime_str[:-1]) if char == digit_str
            ]
            prime_count_size = find_total_primes(prime, digit, positions, prime_list)
            if prime_count_size >= n:
                return prime


if __name__ == "__main__":
    print(solver(8))
