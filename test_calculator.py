import calculator


def test_addition():
    assert calculator.add(2, 5) == 7, "addition is incorrect"


def test_subtraction():
    assert calculator.subtract(4, 2) == 2, "subtraction is incorrect"
