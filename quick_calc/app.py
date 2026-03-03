from __future__ import annotations

from dataclasses import dataclass

from quick_calc.core import add, sub, mul, div


@dataclass
class CalculatorState:
    current: str = "0"            # display text
    pending_op: str | None = None # "+", "-", "*", "/"
    left: float | None = None     # stored left operand
    just_evaluated: bool = False  # after "="
    awaiting_right: bool = False  # after operator, next digit starts a new number


def _format_number(x: float) -> str:
    if float(x).is_integer():
        return str(int(x))
    return str(x)


def _apply_op(op: str, a: float, b: float) -> float:
    if op == "+":
        return float(add(a, b))
    if op == "-":
        return float(sub(a, b))
    if op == "*":
        return float(mul(a, b))
    if op == "/":
        return float(div(a, b))
    raise ValueError(f"Unknown operator: {op}")


def press(state: CalculatorState, token: str) -> CalculatorState:
    """
    token examples: "0"-"9", ".", "+", "-", "*", "/", "=", "C"
    Mutates and returns the same state object.
    """
    token = token.strip()

    # Clear
    if token.upper() == "C":
        state.current = "0"
        state.pending_op = None
        state.left = None
        state.just_evaluated = False
        state.awaiting_right = False
        return state

    # Digit / Dot input
    if token.isdigit() or token == ".":
        # After "=" start fresh
        if state.just_evaluated:
            state.current = "0"
            state.just_evaluated = False

        # After operator, start fresh for right operand
        if state.awaiting_right:
            state.current = "0"
            state.awaiting_right = False

        if token == ".":
            if "." not in state.current:
                state.current = state.current + "." if state.current else "0."
            return state

        # token is digit
        if state.current == "0":
            state.current = token
        else:
            state.current += token
        return state

    # Operator
    if token in {"+", "-", "*", "/"}:
        # If we already have an operation pending and user presses another operator,
        # compute intermediate result using current as right operand.
        if state.pending_op is not None and state.left is not None and not state.awaiting_right:
            right = float(state.current)
            result = _apply_op(state.pending_op, state.left, right)
            state.left = result
            state.current = _format_number(result)
        else:
            state.left = float(state.current)

        state.pending_op = token
        state.just_evaluated = False
        state.awaiting_right = True
        return state

    # Equals
    if token == "=":
        if state.pending_op is None or state.left is None:
            state.just_evaluated = True
            state.awaiting_right = False
            return state

        # If user pressed "=" right after operator (e.g., "5 + ="),
        # treat it as using the current value.
        right = float(state.current)
        result = _apply_op(state.pending_op, state.left, right)

        state.current = _format_number(result)
        state.left = None
        state.pending_op = None
        state.just_evaluated = True
        state.awaiting_right = False
        return state

    raise ValueError(f"Unknown token: {token}")


def evaluate_sequence(tokens: list[str]) -> str:
    """
    Simulate a full user interaction and return final display.
    Example: ["5", "+", "3", "="] -> "8"
    """
    state = CalculatorState()
    for t in tokens:
        press(state, t)
    return state.current