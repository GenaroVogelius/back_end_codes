from time_convert import convert
import pytest

def main():
    test_am_pm()
    test_pm_am()
    test_boths()


def test_am_pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8:50 AM to 4:20 PM") == "08:50 to 16:20"


def test_pm_am():
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("8:50 PM to 4:20 AM") == "20:50 to 04:20"

def test_boths():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("8 PM to 4 AM") == "20:00 to 04:00"
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 17 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 17:80 PM")
    with pytest.raises(ValueError):
        convert("nueve am a 5pm")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")