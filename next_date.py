def main():
    day, month, year = get_input()
    next_day, next_month, next_year = conditions(day, month, year)
    print_values(day, month, year, next_day, next_month, next_year)


def get_input():
    while True:
        try:
            # Get input from the user
            day = int(input('Enter day: '))
            if day < 1 or day > 31:
                raise ValueError('Invalid day.')

            month = int(input('Enter month: '))
            if month < 1 or month > 12:
                raise ValueError('Invalid month.')

            year = int(input('Enter year: '))

            # Check if the day is valid for the given month
            if month == 2:
                if day > 29:
                    raise ValueError("Invalid day for February.")
                elif day == 29 and not search_leap_year(year):
                    raise ValueError("Invalid day for February in non-leap year.")
            elif month in [4, 6, 9, 11] and day > 30:
                raise ValueError("Invalid day for this month.")

            return day, month, year
        except ValueError as e:
            print(e)


# Function to see if a year is a leap year or not
def search_leap_year(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


def conditions(day, month, year):
    # Conditions for February
    if month == 2:
        if day == 28:
            if search_leap_year(year):
                next_day = 29
                next_month = month
                next_year = year
            else:
                next_day = 1
                next_month = month + 1
                next_year = year
        elif day == 29:
            if search_leap_year(year):
                next_day = 1
                next_month = month + 1
                next_year = year
            else:
                raise ValueError("Invalid day for February in non-leap year.")
        else:
            next_day = day + 1
            next_month = month
            next_year = year

    # Conditions for months with 30 days
    elif month in [4, 6, 9, 11]:
        if day == 30:
            next_day = 1
            next_month = month + 1
            next_year = year
        else:
            next_day = day + 1
            next_month = month
            next_year = year

    # Conditions for months with 31 days
    else:
        if day == 31:
            next_day = 1
            next_month = 1 if month == 12 else month + 1
            next_year = year + 1
        else:
            next_day = day + 1
            next_month = month
            next_year = year
    return next_day, next_month, next_year


def print_values(day, month, year, next_day, next_month, next_year):
    print(f'If you are on {day}/{month}/{year}, the next date will be {next_day}/{next_month}/{next_year}.')


if __name__ == '__main__':
    main()