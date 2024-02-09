"""
    Module name :- solution
    Method(s) :- get_name_sum(name), solver(filename), answer()
"""


def get_name_sum(name):
    """
    Find the sum of values of alphabets in name.

    Args:-
        name(str):- Name.

    Return
        Sum of values of alphabets in name.
    """
    names_num = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }

    name_sum = 0

    for alpha in name:
        name_sum += names_num.get(alpha.lower())

    return name_sum


def solver(filename: str):
    """
    Find the sum of product of value and index of names in given file.

    Args:-
        filename(str):- Filename.

    Return
        Sum of product of value and index of names in given file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()

    names = [
        name[1 : len(name) - 1] if "\n" not in name else name[1 : len(name) - 2]
        for name in data.split(",")
    ]

    names_sum = 0
    for index, name in enumerate(sorted(names), start=1):
        names_sum += get_name_sum(name) * index

    return names_sum


def answer():
    """
    Find the sum of product of value and index of names in 'names.txt'.

    Return
        Sum of product of value and index of names in 'names.txt'.
    """
    return solver("math022/names.txt")


if __name__ == "__main__":
    print(f"answer() = {answer()}")
