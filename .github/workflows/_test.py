import pytest

def square(n):
    return n * n
def cube(n):
    return n * n * n

def fifth_power(n):
    return n ** 5

def test_square():
    assert square(2) == 4, "square of 2 should be 4"
    assert square(3) == 9, "square of 3 should be 9"
    assert square(0) == 0, "square of 0 should be 0"

def test_cube():
    assert cube(2) == 8, "cube of 2 should be 8"
    assert cube(3) == 27, "cube of 3 should be 27"
    assert cube(0) == 0, "cube of 0 should be 0"

def test_fifth_power():
    assert fifth_power(2) == 32, "fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "fifth power of 3 should be 243"
    assert fifth_power(0) == 0, "fifth power of 0 should be 0"  

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")