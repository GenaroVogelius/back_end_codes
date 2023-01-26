from patente import is_valid

def main():
        test_lenletters()
        test_numbers()
        test_puntuaction()
        test_numberposition()


def test_lenletters():
        assert is_valid("cs50") == True
        assert is_valid("c") == False

def test_numbers():
        assert is_valid("cs50") == True
        assert is_valid("cs05") == False
        assert is_valid("25") == False
        assert is_valid("1cs50") == False
        assert is_valid("cs50p") == False

def test_puntuaction():
        assert is_valid("cs50!") == False
        assert is_valid("cs,50") ==False
        assert is_valid("cs32") ==True

def test_numberposition():
        assert is_valid("4cs50") == False
        assert is_valid("c5slp50") == False
        assert is_valid("cs32") ==True



if __name__ == "__main__":
        main()
