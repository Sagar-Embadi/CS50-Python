from fuel import convert, gauge
import pytest

def main():
    test_zero_division()
    test_valueError()
    test_correct_input()

# test zeroDivisionError
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


# test valueError
def test_valueError():
    with pytest.raises(ValueError):
        convert('cat/dog')


# test correct input
def test_correct_input():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/2') == 50 and gauge(50) =='50%'
    assert convert('0/4') == 0 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

