# The objetive was to implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
# You may not import any other libraries besides re.
#make a pytest. 

import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    ip = ip.split(".")
    for i in ip:
        if re.fullmatch(r"[0-9]|[0-9][0-9]|[0-1][0-9][0-9]|[0-2][0-4][0-9]|[0-2][0-5][0-5]", i): 
            ok = True #[0-9][0-9] seria del 0 al 99, pones cada [] separado porque i puede ser un numero de 1 digito o de 3 digitos.
        else:
            return False
    if ok == True:
        return True

if __name__ == "__main__":
    main()
