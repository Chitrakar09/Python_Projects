import re


def is_valid(expr):

    # check for allowed characters
    checks = [
        r"^[0-9+\-*/()\s]+$",  # allowed chars
    ]

    if not re.fullmatch(checks[0], expr):
        return False

    # check if there is valid number of parenthesis
    count = 0
    for char in expr:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

        if count < 0:
            return False

    # check if there are any invalid operator patterns
    invalid_patterns = [
        r"[+\-*/]{2,}",  # consecutive operators
        r"^[+*/]",  # starts with invalid operator
        r"[+\-*/]$",  # ends wit operator
        r"\(\s*\)",  # empty parenthesis
        r"\([+\-*/]",  # operator immediately after opening parenthesis
        r"[+\-*/]\)",  # operator immediately before closing parenthesis
        r"\d+\s*\(",  # number immediately followed by opening parenthesis
        r"\)\s*\d",  # closing parenthesis immediately followed by a number
    ]

    for pattern in invalid_patterns:
        if re.search(pattern, expr):
            return False

    return True


def get_precedence(operator):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    return precedence.get(operator, 0)


def infix_to_postfix(expression):
    operators = []
    postfix = []
    tokens = re.findall(r"\d+|[()+\-*/]", expression)

    for token in tokens:

        if re.fullmatch(r"^\d+$", token):
            postfix.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            while operators and operators[-1] != "(":
                postfix.append(operators.pop())

            operators.pop()

        elif token in "+-*/":

            while (
                operators
                and operators[-1] != "("
                and get_precedence(operators[-1]) >= get_precedence(token)
            ):
                postfix.append(operators.pop())

            operators.append(token)

    while operators:
        postfix.append(operators.pop())
    return postfix


def evaluate_postfix(postfix):
    operands = []
    for char in postfix:
        if re.fullmatch(r"^\d+$", char):
            operands.append(char)
        elif char in "+-*/":
            operations = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a / b,
            }
            operand2 = int(operands.pop())
            operand1 = int(operands.pop())
            result = operations[char](
                operand1, operand2
            )  # access the char key in the dictionary and gives us the function which has the arguments operand1 and operand2
            operands.append(result)

    return operands[0]


def evaluate(expression):
    # Infix to postfix
    postfix = infix_to_postfix(expression)

    # evaluate_postfix
    result = evaluate_postfix(postfix)

    return result


class calculator:
    def __init__(self):
        self.result = None
        self.history = {}

    def calculateNewExpression(self):
        while True:
            result = None
            expression = input("What would you like to calculate? (e.g., 5+7*10): ")
            if not is_valid(expression):
                print(
                    "Invalid expression syntax. Please enter a valid mathematical expression"
                )
                continue
            else:
                try:
                    result = evaluate(expression)
                    print("Answer=", result)
                except SyntaxError:
                    print("Invalid expression.")
                    continue
                except ZeroDivisionError:
                    print("Cannot divide by zero.")
                    continue
                finally:
                    self.result = result
                    self.history[f"{expression}"] = result
                return

    def operateWithResult(self):
        while True:
            result = self.result
            if result == None:
                result = ""
            print(f"Previous result = {self.result}")
            expression = input(f"What would you like to calculate: {result}")
            concatenatedExpression = str(result) + expression
            if not is_valid(concatenatedExpression):
                print(
                    "Invalid expression syntax. Please enter a valid mathematical expression"
                )
                continue
            else:
                try:
                    result = evaluate(concatenatedExpression)
                    print("Answer=", result)
                except SyntaxError:
                    print("Invalid expression.")
                    continue
                except ZeroDivisionError:
                    print("Cannot divide by zero.")
                    continue
                finally:
                    self.result = result
                    self.history[f"{concatenatedExpression}"] = result
                return

    def viewHistory(self):
        print("History:")
        if 0 == len(self.history):
            print("Empty")
            return
        for expression, result in self.history.items():
            print(f"{expression}={result}")
        return


def showOptions():
    print("=" * 51)
    print(f"|{'Options':^49}|")
    print(f"|{' 1. Enter expression to calculate':49}|")
    print(f"|{' 2. Operate with result':49}|")
    print(f"|{' 3. View history':49}|")
    print(f"|{' 4. Exit':49}|")
    print("=" * 51)


def main():
    calc = calculator()
    # intro
    print("=" * 12, "WELCOME TO CLI CALCULATOR", "=" * 12)
    print("=" * 51)

    # available operations
    print(f"|{'Available Operations':^49}|")
    print("=" * 51)

    operations = {"Addition": "+", "Subtraction": "-", "Multiply": "*", "Divide": "/"}

    for operation, operator in operations.items():
        print(f"|{operation:^24}|{operator:^24}|")
    print("=" * 51)

    # Options
    while True:
        showOptions()
        try:
            getOptions = int(
                input("Select an option(number corresponding to your choice):")
            )
        except ValueError:
            print("Please enter the number corresponding to your choice")
            continue

        match getOptions:
            case 1:
                calc.calculateNewExpression()
            case 2:
                calc.operateWithResult()
            case 3:
                calc.viewHistory()
            case 4:
                print("="*51)
                print("Thanks for calculating with us. See you next time!")
                print("="*51)
                break
            case _:
                raise ValueError("Please enter a valid option")


if __name__ == "__main__":
    main()
