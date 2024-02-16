def add(a, b):
    """
        Add numbers.
    """
    num, den = b.split('/')
    numerator = int(den) * a + int(num)
    return f'{den}/{str(numerator)}'

def solver(n):
    """
        solver().
    """
    count = 0
    for i in range(1, n+1):
        val = '1/2'
        for j in range(1, i+1):
            if j == i:
                val = add(1, val)
            else:
                val = add(2, val)

        den, num = val.split('/')

        if len(num) > len(den):
            count += 1

    return count

def answer():
    """
        answer().
    """
    return solver(1000)


if __name__ == '__main__':
    print(f'answer() = {answer()}')