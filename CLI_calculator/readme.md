# CLI Calculator

Overview
-
This is a small command-line calculator implemented in `calculator.py`. It parses and evaluates arithmetic expressions written in infix notation, supports parentheses, and maintains a simple calculation history.

How it works
-
- Validates expressions to allow digits, operators (`+ - * /`) and parentheses.
- Converts infix expressions to postfix (Reverse Polish Notation) and evaluates the result.
- Keeps the most recent result and a history of expressions and results.

Usage
-
Run from the repository root:

```bash
python CLI_calculator/calculator.py
```

Once running, choose from the menu to enter an expression, operate using the previous result, view history, or exit.

Notes
-
- Targets Python 3.8+.
- No external dependencies required.
- Be mindful of division by zero and invalid input — the program handles these cases with user-friendly messages.

