# The objetive was to implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError
# Make a pytest code


def main():
        while True:
                try:
                        fraction = input ("Fraction: ")
                        spliti =  (fraction.split("/"))
                        J = int (spliti[0]) 
                        P = int (spliti[1]) 
                        if J > P:
                                raise ValueError
                        percent = int (round(((J / P) *100)))
                        if percent <= 1:
                                print ("E")
                                break
                        if percent >= 99:
                                print ("F")
                                break
                        print (f"{percent}%")
                        break
                
                except ValueError:
                        continue
                except ZeroDivisionError:
                        continue

if __name__ == "__main__":
        main()