from typing import Union, Sequence

Num = Union[int, float]


def add(first_term: Num, second_term: Num) -> Num:
    return first_term + second_term


def subtract(first_term: Num, second_term: Num) -> Num:
    return first_term - second_term


def vec_sum(vec: Sequence[Num]) -> Num:
    s: Num = 0.0
    for ele in vec:
        s += ele
    return s
