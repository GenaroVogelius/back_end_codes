# The objetive was to implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
# Make a pytest code

def main():
        frase = input("Introduce una frase: ")
        frase_corta = (shorten(frase))
        print (f"Output: {frase_corta}")

def shorten(frase):
        vocales =["a","e","i","o","u"]

        frasedividida = list(frase)
        nueva_frase = ""

        for vocal in vocales:
                if vocal in frasedividida:
                        contador = frase.count(vocal)
                        for _ in range(contador):
                                frasedividida.remove(vocal)
                if vocal.upper() in frasedividida:
                        contador = frase.count(vocal.upper())
                        for _ in range(contador):
                                frasedividida.remove(vocal.upper())
                else:
                        continue

        for letras in frasedividida:
                nueva_frase += letras
                #nueva_frase+= "e" #error para testar que test_twtter_gena.py
        return nueva_frase


if __name__ == "__main__":
        main()






