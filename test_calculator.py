from calculator import add, sub, mul, div

def test_add():
    assert add(2, 2) == 4

def test_sub():
    assert sub(5, 5) == 0

def test_mul():
    assert mul(4, 2) == 8

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    assert div(10, 0) == "Error"
