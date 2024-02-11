"""
    Find consecutive prime sum.
"""


def find_all_primes(n):
    """
    Find all prime numbers below n.
    """
    all_primes = []
    for num in range(2, n):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            all_primes.append(num)
    return all_primes


def solver(n):
    """
    Find number which has maximum consecutive primes
    below n.
    """
    all_primes = find_all_primes(n)
    list_len = len(all_primes)
    prime_dict = {}

    for index, prime in enumerate(all_primes[: list_len - 1]):
        idx = index + 1
        prime_list = [prime]

        while idx < list_len:
            prime_list.append(all_primes[idx])
            prime_sum = sum(prime_list)

            if prime_sum > n:
                break

            if prime_sum in all_primes:
                length = len(prime_list)
                prime_dict[prime_sum] = (
                    length
                    if length >= prime_dict.get(prime_sum, 0)
                    else prime_dict[prime_sum]
                )

            idx += 1

    return sorted(prime_dict.items(), key=lambda x: x[1], reverse=True)[0][0]


def answer():
    """
    Find number which has maximum conecutive primes
    below 1000000.
    """
    return solver(1000000)


if __name__ == "__main__":
    print(f"answer()={answer()}")
