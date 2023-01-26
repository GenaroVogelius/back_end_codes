# The objetive was to implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM

# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
# You may not import any other libraries besides re.
# make a pytest code


import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        diccionario = {
            '1':'13',
            '2':'14',
            '3':'15',
            '4':'16',
            '5':'17',
            '6':'18',
            '7':'19',
            '8':'20',
            '9':'21',
            '10':'22',
            '11':'23',
            '12':'12'}
        matches = re.fullmatch(r"(.+)\sPM\sto\s(.+)AM|(.+)\sAM\sto\s(.+)?\sPM", s)
        if matches.group(3) and matches.group(4):
            am = matches.group(3).strip()
            pm = matches.group(4).strip()
            if not ":" in pm:
                minutosPM = "00"
                horaPM = pm
            else:
                horaPM, minutosPM = pm.split(":")
                if int(minutosPM) >= 60:
                    raise ValueError

            if not ":" in am:
                minutosAM = "00"
                if am == "12":
                    am = "00"
                horaAM = am
            else:
                horaAM, minutosAM = am.split(":")
                if horaAM == "12":
                    horaAM = "00"

            hora_convertida = diccionario[horaPM]
            pm = f"{hora_convertida}:{minutosPM}"
            if len(horaAM) <= 1:
                horaAM = f"0{horaAM}"
            am = f"{horaAM}:{minutosAM}"
            return(f"{am} to {pm}")

        if matches.group(1) and matches.group(2):
            am = matches.group(2).strip()
            pm = matches.group(1).strip()
            if not ":" in pm:
                minutosPM = "00"
                horaPM = pm
            else:
                horaPM, minutosPM = pm.split(":")

            if not ":" in am:
                minutosAM = "00"
                if am == "12":
                    am = "00"
                horaAM = am
            else:
                horaAM, minutosAM = am.split(":")
                if horaAM == "12":
                    horaAM = "00"

                if int(minutosPM) >= 60:
                    raise ValueError

            hora_convertida = diccionario[horaPM]
            pm = f"{hora_convertida}:{minutosPM}"
            if len(horaAM) <= 1:
                horaAM = f"0{horaAM}"
            am = f"{horaAM}:{minutosAM}"
            return(f"{pm} to {am}")
    except:
        raise ValueError
if __name__ == "__main__":
    main()




