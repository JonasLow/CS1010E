from Week_03_1 import staircase
import pytest

def main():
    test_cases()
    test_string()
    test_negative()

def test_cases():
    assert staircase(1) == 1
    assert staircase(2) == 2
    assert staircase(3) == 3
    assert staircase(10) == 89

def test_string():
    with pytest.raises(TypeError):
        staircase('cat')

def test_negative():
    with pytest.raises(ValueError):
        staircase(-42)
        staircase(0)

if __name__ == "__main__":
    main()
