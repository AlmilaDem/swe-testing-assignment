# Testing Strategy (Quick-Calc)

This document describes the testing approach for Quick-Calc, based on concepts from Lecture 3 (Software Engineering & Testing).

## What was tested

### Unit tests (core logic)

Unit tests target `quick_calc/core.py` to verify each operation in isolation:

* Addition, subtraction, multiplication, division
* Edge cases: division by zero, negative numbers, decimals, very large values

### Integration tests (input layer + core together)

Integration tests target `quick_calc/app.py` via `evaluate_sequence(tokens)` to verify the interaction between the input layer and calculation logic:

* Full user flow: `5 + 3 =` results in `8`
* Clear (C) after a calculation resets the display to `0`
* Division by zero through the input flow raises a controlled error (`ZeroDivisionError`)

## What was not tested (and why)

* **GUI testing**: The focus is testing strategy and code quality. A heavy UI was intentionally avoided; the token-based input layer serves as a simple interface for integration tests.
* **Non-functional testing** (performance, security, usability, accessibility): Out of scope for this small calculator. Priority is functional correctness and maintainable tests.

## Lecture concept mapping

### 1) Testing Pyramid

The suite follows the Testing Pyramid: **many unit tests** for the smallest pieces (core functions) and **fewer integration tests** to validate end-to-end behavior through the input layer.

### 2) Black-box vs White-box testing

* **Unit tests** are mostly *white-box* because they directly call internal functions (`add`, `sub`, `mul`, `div`) and check expected outputs and exceptions.
* **Integration tests** are closer to *black-box* because they simulate user actions via token sequences and validate the final display result without relying on internal implementation details.

### 3) Functional vs Non-Functional testing

This project focuses on **functional testing** (correct calculation results, clear/reset behavior, and division-by-zero handling). It intentionally does not include non-functional tests such as performance benchmarks or UI accessibility due to scope.

### 4) Regression testing

The test suite can be rerun after any code change (`pytest`) to ensure previously working behavior still works. In a real project, these tests would run automatically in CI for every pull request to prevent regressions.

## Test results summary

Run:
pytest

| Test name                                   | Type        | Status |
| ------------------------------------------- | ----------- | ------ |
| test_addition_basic                         | Unit        | Pass   |
| test_subtraction_basic                      | Unit        | Pass   |
| test_multiplication_basic                   | Unit        | Pass   |
| test_division_basic                         | Unit        | Pass   |
| test_division_by_zero_raises                | Unit        | Pass   |
| test_negative_numbers                       | Unit        | Pass   |
| test_decimal_addition                       | Unit        | Pass   |
| test_very_large_numbers                     | Unit        | Pass   |
| test_full_addition_flow                     | Integration | Pass   |
| test_clear_resets_after_calculation         | Integration | Pass   |
| test_division_by_zero_is_handled_gracefully | Integration | Pass   |
