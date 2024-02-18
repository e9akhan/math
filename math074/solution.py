"""
    Math 74
"""


def factorial(n):
    """
    Factorial.
    """
    fact = 1

    for i in range(2, n + 1):
        fact *= i
    return fact


def solver(n, key):
    """
    solver(n, key).
    """
    factorials = {str(i): factorial(i) for i in range(10)}

    fact_chain = {}

    for i in range(1, n):
        num = i
        fact_list = [i]
        val = 0

        while True:
            val = 0
            for digit in str(num):
                val += factorials[digit]

            if val in fact_list:
                break

            fact_list.append(val)
            num = val

        length = len(fact_list)
        fact_chain[length] = fact_chain.get(length, []) + [i]

    return len(fact_chain[key])


def answer():
    """
    answer().
    """
    return solver(1000000, 60)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
