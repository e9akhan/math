"""
    Find how many words in words.txt are triangle words.
"""

WORDS_NUM = {
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


def is_triangle_number(number):
    """
    Check whether the given number is triangle number or not.
    """
    n = 1
    triangle_number = 0

    while triangle_number < number:
        triangle_number = 0.5 * n * (n + 1)
        n += 1

    if triangle_number == number:
        return True
    return False


def solver():
    """
    Find how many triangle numbers are in words.txt file
    """
    with open("math042/words.txt", "r", encoding="utf8") as f:
        words = f.read()

    word_list = [word[1 : len(word) - 1] for word in words.split(",")]
    triangle_word_numbers = []
    count = 0

    for word in word_list:
        word_sum = sum(WORDS_NUM[alpha] for alpha in word.lower())

        if word_sum in triangle_word_numbers:
            count += 1
            continue

        if is_triangle_number(word_sum):
            triangle_word_numbers.append(word_sum)
            count += 1

    return count


def answer():
    """
    Find how many triangle numbers are in words.txt file
    """
    return solver()


if __name__ == "__main__":
    print(f"answer()={answer()}")
