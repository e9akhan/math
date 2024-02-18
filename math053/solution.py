"""
    Math 53
"""


def solver(num, end):
    """
    solver()
    """
    fact_dict = {0: 1, 1: 1}
    count = 0

    if num in fact_dict:
        return fact_dict[num]

    for n in range(2, num + 1):
        fact_dict[n] = fact_dict[n - 1] * n

        for r in range(1, n // 2 + 1):
            val = fact_dict[n] // (fact_dict[r] * fact_dict[n - r])

            if val > end:
                if n % 2 == 0 and r == n // 2:
                    count += 1
                else:
                    count += 2

    return count


def answer():
    """
    Find combinations having values more than 1e6.
    """
    return solver(100, 1e6)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
