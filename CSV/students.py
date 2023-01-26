# The objetive was to implement a program that:
# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

#In order to try the programm you can input on the terminal python students.py beforestudents.csv after.csv, being beforestudents.csv the spreadsheet you would like to change, and after.csv the spreadsheet where you would like to have the new changes. 

import sys
import csv

def main():
        if len(sys.argv) == 3:
                try:
                        contador = 0
                        with open(sys.argv[1], 'r') as csv_file:
                                csv_reader = csv.DictReader (csv_file)
                                with open (sys.argv[2], "w", newline="") as nuevo_csv:
                                        for row in csv_reader:
                                                last,first = row ["name"].split(", ")
                                                house = row["house"]
                                                fieldnames = ['first', 'last', 'house']
                                                writer = csv.DictWriter (nuevo_csv, fieldnames = fieldnames)
                                                if contador == 0:
                                                        writer.writeheader()
                                                contador += 1
                                                writer.writerow({"first": first, "last": last, "house": house})

                except FileNotFoundError:
                        sys.exit("Could not read invalid_file.csv")
        elif len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")
        elif len(sys.argv) <= 2:
                sys.exit ("Too few command-line arguments")

if __name__ == "__main__":
        main()