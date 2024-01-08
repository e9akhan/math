"""
    Module name :- solution
    Method(s) :- answer(), is_prime(year), solver(from_date, to_date, weekday)
"""

import datetime


def is_prime(year):
    """
    Checks whether the given year is prime or not.

    Args:-
        year(int) :- Year

    Return
        Whether the given year is prime or not.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def solver(from_date: datetime.date, to_date: datetime.date, weekday):
    """
    Find the num of times the given weekday comes on 1st of month.

    Args:-
        from_date(datetime) :- Starting date.
        to_date(datetime) :- Ending date.

    Return
        Num of times the given weekday comes on 1st of month.
    """

    weekdays = {
        "MONDAY": 1,
        "TUESDAY": 2,
        "WEDNESDAY": 3,
        "THURSDAY": 4,
        "FRIDAY": 5,
        "SATURDAY": 6,
        "SUNDAY": 7,
    }

    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    start_day = from_date.day
    end_day = to_date.day

    start_month = from_date.month
    end_month = from_date.month

    start_year = from_date.year
    end_year = to_date.year

    size = weekdays[weekday.upper()]

    count = 0
    extra_count = 0

    for year in range(1900, end_year + 1):
        for month in range(1, 13):
            if is_prime(year) and month == 2:
                days = 29
            else:
                days = months[month]

            for day in range(size, days + 1, 7):
                if start_day <= day and start_month == month and start_year == year:
                    extra_count = count

                if day == 1:
                    count += 1

                if end_day <= day and end_month == month and end_year == year:
                    return count - extra_count

            size = 7 - (days - day)

    return count - extra_count


def answer():
    """
    Find the num of times the given weekday comes on 1st of month in 20th century.

    Args:-
        from_date(datetime) :- Starting date.
        to_date(datetime) :- Ending date.

    Return
        Num of times the given weekday comes on 1st of month in 20th century.
    """
    start_date = datetime.datetime.strptime("01-01-1901", "%d-%m-%Y")
    end_date = datetime.datetime.strptime("31-12-2000", "%d-%m-%Y")
    return solver(start_date, end_date, "SUNDAY")


if __name__ == "__main__":
    current_date = datetime.date.today()
    future_date = datetime.datetime.strptime("01-11-2025", "%d-%m-%Y")
    print(
        f"""
        solver(current_date, future_date, "MONDAY") = {solver(current_date, future_date, "MONDAY")}
    """
    )
    print(f"answer() = {answer()}")
