from contador_um import count

def main():
    test_umword()
    test_noum()
    test_spaceum()

def test_umword():
    assert count("Um, thanks for the album") == 1

def test_noum():
    assert count("yum") == 0

def test_spaceum():
    assert count("  um  ") == 1

if __name__ == "__main__":
    main()