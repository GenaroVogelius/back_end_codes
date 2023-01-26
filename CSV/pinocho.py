# The objetive was to implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

# In order to try the programm you should enter on the terminal python pinocho.py regular.csv and then python pinocho.py sicilian.csv.

import sys
from tabulate import tabulate
import csv


def main():
        
        if len(sys.argv) == 2:
                if sys.argv[1].endswith(".csv") == False:
                        sys.exit("Not a Python file")
                try:
                        with open(sys.argv[1], 'r') as csv_file:
                                csv_reader = csv.DictReader (csv_file, delimiter=",")        
                                print (tabulate(csv_reader, headers="keys", tablefmt="grid"), end="")
                except FileNotFoundError:
                        sys.exit("File does not exist")
        elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments") 
        elif len(sys.argv) <= 1:
                sys.exit ("Too few command-line arguments") 


if __name__== "__main__":
        main()

#headers = csv_reader.fieldnames #si pones fieldnames estas accediendo a las keys del csv.