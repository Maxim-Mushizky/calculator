from src import calc
import pytest
import random
import numpy as np


@pytest.mark.single
@pytest.mark.parametrize(("x", "y"), [(10 * random.random(), 20 * random.random()) for _ in range(20)],
                         ids=[f"Add {i}" for i in range(20)])
def test_add(x, y):
    assert x + y == pytest.approx(
        calc.add(x, y)), f"Addition module is not working properly for x = {x} and y = {y}"


@pytest.mark.single
@pytest.mark.parametrize("x,y", [(10 * random.random(), 20 * random.random()) for _ in range(20)],
                         ids=[f"Subtract {i}" for i in range(20)])
def test_subtract(x, y):
    assert x - y == pytest.approx(
        calc.subtract(x, y)), "Subtract module is not working properly for x = {x} and y = {y}"


@pytest.mark.vector
@pytest.mark.parametrize('v', [
    [random.randint(-1000, 1000000) for _ in range(random.randint(10, 1000))] for _ in range(5)

])
def test_vec_sum(v):
    assert np.sum(v) == calc.vec_sum(v), "The sum module isn't working properly"
