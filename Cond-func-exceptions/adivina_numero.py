# The objetive of the programm was to:
# Prompts the user for a level "N°", If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and "N°", inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

import random

def main():
    try:
        number = int (input ("Level: "))
        numero_adivinar = (random.randrange(1,number))

        while True:
            adivinar = guess(number)
            if adivinar == numero_adivinar:
                print ("Just right!")
                exit(1)
            elif adivinar < numero_adivinar:
                print ("Too small!")
                continue
            elif adivinar > numero_adivinar:
                print ("Too large!")
                continue

    except ValueError:
        main()


def guess(number):
    while True:
        try:
            adivinar = int (input ("Guess: "))
            if adivinar <= 0:
                raise ValueError
            elif adivinar >= number:
                raise ValueError
            else:
                return adivinar

        except ValueError:
            continue

if __name__=="__main__":
    main()