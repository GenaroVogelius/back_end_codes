# The objetive was to implement a program that:
# Prompts the user for a level N°, If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with N° digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.


import random

def main():
        level = get_level()
        score = 0
        contador = 2
        for _ in range (10):
                x , y = generate_integer(level)
                problema = x + y
        for _ in range(3):
                try:
                        respuesta = int (input (f"{x} + {y} = "))
                        if problema == respuesta:
                                score += 1
                                break
                        else:
                                print ("EEE")
                                if contador > 0:
                                        print (f"You may have {contador} tries")
                                contador = contador - 1
                except ValueError:
                        print ("EEE")
                        if contador > 0:
                                print (f"You may have {contador} tries")
                        contador = contador -1
                        continue
                if problema != respuesta:
                        print (f"{x} + {y} = {problema}")
        print (f"Score: {score}")




def get_level():
        while True:
                try:
                        level = int (input ("Level: "))
                        if level == 1 or level == 2 or level == 3:
                                return level
                        else:
                                continue
                except ValueError:
                        continue



def generate_integer(level):
        if level == 1:
                desde = 0
                hasta = 9
        elif level == 2:
                desde = 10
                hasta = 99
        elif level == 3:
                desde = 100
                hasta = 999
        x = random.randint(desde, hasta)
        y = random.randint(desde, hasta)
        return x, y

if __name__ == "__main__":
        main()