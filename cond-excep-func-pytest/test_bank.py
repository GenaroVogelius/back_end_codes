from bank import value

def main():
    test_0()
    test_20()
    test_100()

def test_0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello gena") ==0

def test_20():
    assert value("h") == 20
    assert value("hola") ==20
    assert value("hi") ==20

def test_100():
    assert value("kelou") == 100
    assert value("como va") ==100
    assert value("todo ok") ==100


if __name__ == "__main__":
    main()