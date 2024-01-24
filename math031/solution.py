"""
    Find number of combinations to make an amount using coins.
"""


def combinations(amt, coins):
    """
    Function to find combinations of coins that sum up to amt.
    """
    if amt <= 0:
        return 0

    while amt < coins[0] and len(coins) != 1:
        coins = coins[1:]

    coin = coins[0]
    count = 0

    if coin == 1:
        return count + 1

    itr = amt / coin

    while itr >= 0:
        rem = amt - itr * coin

        if amt == 0:
            count += 1
        else:
            count += combinations(rem, coins[1:])

        itr -= 1

    return count


def solver(amt):
    """
    Number of combinations to make amt using coins.
    """
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    return combinations(amt * 100, coins)


def answer():
    """
    Number of combinations to make 2 euros using coins.
    """
    return solver(2)


if __name__ == "__main__":
    print(f"solver(1) = {solver(1)}")
    print(f"answer() = {answer()}")
