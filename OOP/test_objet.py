from jar import Jar
import pytest


def test_init():
    jar = Jar(4) #aca le estas dando una capacidad de 4
    assert jar.capacity == 4
    assert jar.size == 0
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(1) == 1
    assert jar.deposit(5) == 6
    with pytest.raises(ValueError):
        jar.deposit(80)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert jar.withdraw(1) == 9
    assert jar.withdraw(3) == 6
    with pytest.raises(ValueError):
        jar.withdraw(80)