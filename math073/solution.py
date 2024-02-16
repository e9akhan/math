"""
    Math 73
"""


def gcd(x, y):
    """
        GCD of numbers.
    """
    return y and gcd(y, x%y) or x

def solver(div):
    """
        Find total numbers between 1/3 and 1/2.
    """
    fractions = []
    for d in range(2, div+1):
        for n in range(1, d):
            if gcd(d, n) != 1:
                continue

            fractions.append(f'{n}/{d}')

    fractions = sorted(fractions, key = lambda x: eval(x))
    idx1 = fractions.index('1/3')
    idx2 = fractions.index('1/2')
    return idx2 - idx1 - 1

def answer():
    """
        Find total numbers between 1/3 and 1/2 for 12000.
    """
    return solver(12000)

if __name__ == '__main__':
    print(f'answer() = {answer()}')