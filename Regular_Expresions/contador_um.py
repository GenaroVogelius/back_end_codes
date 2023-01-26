# The objetive was to implement a function called count that expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. For instance, given text like hello, um, world, the function should return 1. Given text like yummy, though, the function should return 0.
# You may not import any other libraries besides re.
# Make a pytest code.

import re

def main():
    print(count(input("Text: ")))

def count(s):
    match = re.findall(r"(\bum\b)", s, re.IGNORECASE)  #\b...\b establece bondaries y va a buscar solamente lo que este dentro de eso, el re.findall te hace una lista de los match que haga.
    contador = 0
    for i in match:
        contador +=1
    return contador

if __name__ == "__main__":
    main()