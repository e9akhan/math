"""
    Math 55
"""


def solver():
    """
    Find lychrel numbers below 10001.
    """
    lychrel_numbers = []
    for i in range(1, 10001):
        num = i
        count = 0

        while count < 50:
            num_rev = int(str(num)[::-1])
            num += num_rev

            if str(num) == str(num)[::-1]:
                break

            count += 1

        if count == 50:
            lychrel_numbers.append(i)

    return len(lychrel_numbers)


def answer():
    """
    answer()
    """
    return solver()


if __name__ == "__main__":
    print(f"answer() = {answer()}")
