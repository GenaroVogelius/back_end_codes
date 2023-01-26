from numero_ok import validate

def main():
    test_true()
    test_false()


def test_true():
    assert validate("127.0.0.8") == True
    assert validate("255.255.251.255") == True

def test_false():
    assert validate("290.0.0.8") == False
    assert validate("255.255.251.256") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("car") == False

if __name__ == "__main__":
    main()
