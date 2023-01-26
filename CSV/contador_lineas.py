# The objetive was to implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

#Para que funciones tenes que poner python contador_lineas.py (FILENAME) siendo filename el nombre del archivo que queres que lea cuantas lineas tiene. In order to try the programm you should enter on the terminal python contador_lineas.py (FILENAME) being filename the name of the directory you want to read how many lines have.


import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith("py") == True:
        try:
            with open(sys.argv[1]) as file:
                lineas = file.readlines()
                contador = 0
                for linea in lineas:
                    if linea.lstrip().startswith("#"):
                        continue
                    if linea.isspace() == True:
                        continue
                    contador += 1
            print (contador, end="")
        except IndexError:
                sys.exit("Not a Python file")
        except FileNotFoundError:
            sys.exit("File does not exist")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) <= 1:
                sys.exit ("Too few command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")

if __name__ == "__main__":
        main()