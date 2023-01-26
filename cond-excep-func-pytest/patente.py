# implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
#make a pytest code

def main():
        plate = input("Plate: ")
        if is_valid(plate):
                print("Valid")
        else:
                print("Invalid")


def is_valid(plate):
        check1 =  letterL(plate)
        if check1 == True:
                check2 = letterNumbers(plate)
                if check2 == True:
                        check3 = psp(plate)
                        if check3 == True:
                                return True
                        else:
                                return False

def letterL(plate):
        if len(plate) >= 2 and len(plate) <= 6:
                return True
def letterNumbers(plate):
        contador = 0
        posicion_numero= []
        while contador <= 9:
                posicion = plate.find(str(contador))
                contador += 1
                if posicion != -1:
                        posicion_numero.append(posicion)
        if posicion_numero == []:  #En el caso de que no haya numeros
                return True
        contador = 0
        for i in posicion_numero:
                if not (len(plate)/2) <= posicion_numero[contador]:
                        return False
                else:
                        contador += 1

        posicion_numero.sort()
        if (plate[posicion_numero[0]]) == "0":
                return False
        else:
                return True

def psp(plate):
        punctuation = ('''!()-[]{};:'"\,<>./?@#$%^&*_~''')
        if punctuation in plate:
                return False
        check = plate.strip()
        if check != plate:
                return False
        else: 
                return True

if __name__ =="__main__":
        main()