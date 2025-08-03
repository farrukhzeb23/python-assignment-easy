operators = ('+', '-', '*', '/')


class InvalidOperator(Exception):
    """Custom exception for practice"""
    pass


def calculate(x, y, operator):
    operations = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x/y
    }
    handler = operations.get(operator)
    return handler(x, y)

    # if operator == '+':
    #     return x+y
    # elif operator == '-':
    #     return x-y
    # elif operator == '*':
    #     return x*y
    # elif operator == '/':
    #     return x/y
    # else:
    #     raise InvalidOperator("Invalid operator")


def get_number_input(prompt_message):
    while True:
        try:
            num = input(prompt_message)
            return float(num)
        except ValueError:
            print("Input your valid numeric number")


def get_operator():
    while True:
        try:
            operator = input("Input your arithematic operator (+, -, *, /): ")
            if operator not in operators:
                raise InvalidOperator("Invalid operator inputted")
            return operator
        except InvalidOperator as error:
            print(error)


while True:
    num_1 = get_number_input("Enter your first number: ")
    num_2 = get_number_input("Enter your second number: ")
    operator = get_operator()
    try:
        print(f"Output: {calculate(num_1, num_2, operator)}")
        break
    except ZeroDivisionError:
        print("You cannot divide by zero please try again")
    except Exception as error:
        print(error)
