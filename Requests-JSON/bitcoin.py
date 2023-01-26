# The objetive was to implement a program that:
# Expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
# Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.

import requests
import json
import sys

try:    
        if len(sys.argv) > 1:
                numero_flotante = float (sys.argv[1])
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                diccionario = response.json()
                A = diccionario["bpi"]
                B = A["USD"]
                C = B["rate_float"]
                amount = (float (C) * (numero_flotante))
                print (f"${amount:,.4f}", end="")
        else:
                print ("Missing command-line argument", end="")
                sys.exit
except:
        print ("Command-line argument is not a number", end="")
        sys.exit




