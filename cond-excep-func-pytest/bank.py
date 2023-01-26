# The objetive was to implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
        greeting = input ("hello ").lower().strip()
        valor = (value(greeting))
        print (f"${valor}")


def value(greeting):
        if greeting.lower().strip().startswith("hello") == True:  #Le tuviste que poner el lower y strip aca para que te salga bien
                return (0)
        elif greeting.lower().strip().startswith("h") == True:
                return (20)
        else:
                return (100)



if __name__ == "__main__":
        main()