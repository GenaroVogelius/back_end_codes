from nafta import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    with pytest.raises(ZeroDivisionError):  #se pone asi para que busque si sale ese error
        convert ("4/0")
    with pytest.raises(ValueError):
        convert("hola/DOG")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

if __name__ == "__main__":
        main()