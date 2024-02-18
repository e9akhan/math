"""
    Math 63
"""


def solver():
    """
    solver()
    """
    count = 0

    for i in range(1, 22):
        for j in range(1, 22):
            val = i**j

            if len(str(val)) == j:
                count += 1


def answer():
    """
    answer()
    """
    return solver()


if __name__ == "__main__":
    print(f"answer() = {answer()}")
