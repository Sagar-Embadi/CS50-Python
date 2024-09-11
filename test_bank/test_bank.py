from bank import value

def main():
    test_return_0()
    test_return_20()
    test_return_100()

def test_return_0():
    assert value('hello') == 0
    assert value('HELLO') == 0

def test_return_20():
    assert value('hey') == 20

def test_return_100():
    assert value("what's up!") == 100

if __name__ == "__main__":
    main()
