"""
    Math 72
"""


def gcd(x, y):
    """
        GCD of numbers.
    """
    return y and gcd(y, x%y) or x

def solver(div):
    """
        Find total numbers bof elements.
    """
    count = 0
    for d in range(2, div+1):
        for n in range(1, d):
            if gcd(d, n) != 1:
                continue

            count += 1
    return count

def answer():
    """
        Find total number of elements for 1000000.
    """
    return solver(1000000)

if __name__ == '__main__':
    print(f'answer() = {answer()}')