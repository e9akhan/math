"""
    Module name :- solution
    Method(s) :- solver(a, b), answer()
"""


def solver(a: int = None, b: int = None):
    """
    Find the total numbers of letters in words of numbers over a range.

    Args:-
        a(int):- Starting point of range.
        b(int) :- Ending point of range

    Return
        Total numbers of letters in words of numbers over a range
    """
    words = {
        0: "",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE",
        10: "TEN",
        11: "ELEVEN",
        12: "TWELVE",
        13: "THIRTEEN",
        14: "FOURTEEN",
        15: "FIFTEEN",
        16: "SIXTEEN",
        17: "SEVENTEEN",
        18: "EIGHTEEN",
        19: "NINETEEN",
        20: "TWENTY",
        30: "THIRTY",
        40: "FORTY",
        50: "FIFTY",
        60: "SIXTY",
        70: "SEVENTY",
        80: "EIGHTY",
        90: "NINETY",
        1000: "THOUSAND",
        1000000: "MILLION",
        1000000000: "BILLION",
    }

    start = 1
    end = a or b

    if a and b:
        start = a
        end = b

    count = 0

    for number in range(start, end + 1):
        num_str = str(number)
        length = len(num_str)
        j = length - 1
        string = ""

        while j >= 0:
            num_int = int(num_str[: j + 1])

            units_place = length - j

            remainder = num_int % 10

            if string and units_place == 3:
                string = "AND" + string

            if units_place % 3 == 0 and remainder:
                string = "HUNDRED" + string

            if (
                (remainder or num_str[j - 1])
                and 10 ** (units_place - 1) in words
                and j < length - 3
            ):
                string = words[10 ** (units_place - 1)] + string

            if (units_place - 1) % 3 == 0:
                remainder = num_int % 100
                if remainder < 21:
                    string = words[remainder] + string
                else:
                    remainder1 = num_int % 10
                    string = words[remainder1] + string
                    remainder -= remainder1
                    string = words[remainder] + string
                j -= 2
                continue

            if j >= 0:
                string = words[remainder] + string

            j -= 1

        count += len(string)

    return count


def answer():
    """
    Find the total numbers of letters in words of numbers from 1-1000.

    Return
        Total numbers of letters in words of numbers from 1-1000.
    """
    return solver(1, 1000)


if __name__ == "__main__":
    print(f"solver(1, 5) = {solver(1, 5)}")
    print(f"answer() = {answer()}")
