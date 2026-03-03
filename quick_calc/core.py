from __future__ import annotations

Number = float | int


def add(a: Number, b: Number) -> Number:
    return a + b


def sub(a: Number, b: Number) -> Number:
    return a - b


def mul(a: Number, b: Number) -> Number:
    return a * b


def div(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b