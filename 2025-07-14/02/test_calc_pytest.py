import pytest
from calc import Calculator
@pytest.fixture 
def calculator():   
    c = Calculator()
    yield c
    # Teardown code can be added here if needed
    del c

def test_add(calculator):   
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract(calculator):
    assert calculator.subtract(2, 1) == 1
    assert calculator.subtract(1, 2) == -1
    assert calculator.subtract(-1, -1) == 0

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 5) == -5
    assert calculator.multiply(0, 100) == 0

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, -3) == 2
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

def test_divide_negative(calculator):
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(6, -3) == -2
    with pytest.raises(ValueError):
        calculator.divide(0, 0)

# The code snippets from both files are identical, so no changes are needed.