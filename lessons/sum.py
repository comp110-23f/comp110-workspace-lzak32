"""Summing the elements of a list using different loops."""
__author__ = "730679428"


def w_sum(vals: list[float]) -> float:
    """Sums the elements of a list of floats using a while loop."""
    sum: float = 0.0
    i: int = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums the elements of a list of floats using a for ... in loop."""
    sum: float = 0.0
    for x in vals:
        sum += x
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums the elements of a list of floats using a for ... in range() loop."""
    sum: float = 0.0
    for x in range(len(vals)):
        sum += vals[x]
    return sum