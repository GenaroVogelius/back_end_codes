# The objetive was to implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
# Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.
# Make a pytest code.

# Example of valid input:
# 1999-01-01


from datetime import date
import inflect
import sys


def main():
        birthday = input ("Date of birth: ")
        print (minutes(birthday))
def minutes(birthday):
    try:
        year, mounth, day = birthday.split("-")
        if birthday.count("-") != 2:
            sys.exit("Invalidad date")
        elif len(birthday) != 10:
            sys.exit("Invalidad date")

    except ValueError:
        sys.exit("Invalidad date")

    cumpleaños = date(int(year), int(mounth), int(day))
    hoy = date.today()
    diferencia = hoy - cumpleaños
    minutos = int (diferencia.total_seconds() // 60)
    p = inflect.engine()
    words = p.number_to_words(minutos, andword="") + (" minutes")
    return words.capitalize()

if __name__ == "__main__":
    main()