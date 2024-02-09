"""
    Find the product of d[1]*d[10]*..*d[1000000]
    where d[i] represent number at ith position in decimal
    part of n digit.
"""


def solver():
    """
    Find the product of d[1]*d[10]*..*d[1000000]
    where d[i] represent number at ith position in decimal
    part of n digit.
    """
    decimal = ""
    number = 1

    while len(decimal) < 1000000:
        decimal += str(number)
        number += 1

    return (
        int(decimal[0])
        * int(decimal[9])
        * int(decimal[99])
        * int(decimal[999])
        * int(decimal[9999])
        * int(decimal[99999])
        * int(decimal[999999])
    )


def answer():
    """
    answer()
    """
    return solver()


if __name__ == "__main__":
    print(f"answer() = {answer()}")
