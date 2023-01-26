#  The objetive was to implement a program that prompts the user for names, one per line, until the user inputs control-d on mac or control-z on windows. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and N° names with N° -1 commas and one and, as in the below:

import inflect
p = inflect.engine()

lista = []
while True:
    try:
        lista.append(input ("Name: " ))
    except EOFError:
        mylist = p.join(lista, final_sep="")
        print(f"Adieu, adieu, to {mylist}")
        break


#you can also use this library in this cases:
# word= "worker"
# print("The plural of ", word, " is ", p.plural(word))

# cat_count = 1 
# print("I saw", cat_count, p.plural("cat", cat_count))