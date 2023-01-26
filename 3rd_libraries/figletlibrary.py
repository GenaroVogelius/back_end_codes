# The objetive was to implement a program that:
# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

#in order to try the programm you should input on the terminal python figletlibrary.py -f slant, then write whatever you want. You can also enter on the terminal python figletlibrary.py -f rectangles and then write whatever you want to see the results.

import sys
import random
from pyfiglet import Figlet

if 1 == len(sys.argv):
    randomfont = True
if 3 == len(sys.argv) and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    randomfont = False
else:
    sys.exit ("Invalid usage")

figlet = Figlet()
figlet.getFonts()


if randomfont == False:
    try:
        figlet.setFont(font=sys.argv[2])
        string = input("Input: ")
        print(figlet.renderText(string))
    except:
        sys.exit ("Invalid usage")

if randomfont == True:
    try:
        aleatorio = random.choice(figlet.getFonts())
        string = input("Input: ")
        print(figlet.renderText(aleatorio))
    except:
        sys.exit ("Invalid usage")