# Quick-Calc (SWE Testing Assignment)

Quick-Calc is a small calculator application created for the Advanced Software Engineering course (Lecture 3 — Software Engineering & Testing). It supports addition, subtraction, multiplication, division (with safe handling of division by zero), and a clear (C) operation. The focus of this project is clean, testable code, a multi-layered test strategy, and professional Git/GitHub workflow.

## Features

* Addition, subtraction, multiplication, division
* Division by zero handled gracefully (raises a controlled `ZeroDivisionError`)
* Clear (C) resets the calculator state to `0`
* Unit + integration tests runnable with one command

## Project Structure

```
quick_calc/
  core.py
  app.py
tests/
  test_unit_core.py
  test_integration_app.py
```

## Setup

### Using GitHub Codespaces (recommended)

1. Open the repository in Codespaces
2. Install dependencies:

```
pip install -r requirements.txt
```

### Local setup

1. Install Python 3.10+ and Git
2. Install dependencies:

```
pip install -r requirements.txt
```

## Run the app

```
python -c "from quick_calc.app import evaluate_sequence; print(evaluate_sequence(['5','+','3','=']))"
```

## How to Run Tests

```
pytest
```

## Testing Framework Research: Pytest vs Unittest

Python provides `unittest` in the standard library, while `pytest` is a popular third-party framework. `unittest` is class-based and includes concepts like test cases and setup/teardown methods. It is reliable but requires more boilerplate code, which can make tests longer and harder to read.

`pytest` uses simple assert statements, has better automatic test discovery, and provides powerful features such as fixtures and parametrization. It also produces more readable output and allows developers to write tests faster with less code.

This project uses pytest because it is simpler, cleaner, and more efficient for writing and maintaining tests in a small-to-medium sized project like Quick-Calc.
