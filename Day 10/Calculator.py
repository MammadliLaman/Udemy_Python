# Creat a calculator

from art import logo


# Add


def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


math_operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    for operator in math_operators:
        print(operator)
    is_continue = True

    while is_continue:
        operator_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the next number: "))
        calculation = math_operators[operator_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with the {answer}, or type 'n' to start calculation again: ") == 'y':
            num1 = answer
        else:
            is_continue = False
            calculator()


calculator()












# value = operator[key]

# if operator_symbol == "+":
#     answer = add(num1, num2)
# elif operator_symbol == "-":
#     answer = subtract(num1, num2)
# elif operator_symbol == "*":
#     answer = multiply(num1, num2)
# else:
#     answer = divide(num1, num2)