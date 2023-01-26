from pruebas.pruebas_de_gena import shorten #aca importas la función
#    aca importas el archivo

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("CS50") == "CS50"

if __name__ == "__main__":
    main()

#Para usar pytest pone pytest test_twtter.py