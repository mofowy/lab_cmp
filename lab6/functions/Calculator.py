from lab6.functions.calcFunctions import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation, PowerOperation, SqrtOperation, ModulusOperation
from lab6.init import memory, app_settings
import lab6.constants.constants as const

class Calculator:
    def __init__(self):
        self.history = []
        self.result = None

    def log_to_file(self, expression, result):
        try:
            with open("lab6/logs/calculator_history.txt", "a") as logFile:
                logFile.write(f"{expression} = {result}\n")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            
    def get_input(self):
        return input("Enter an expression (e.g., '5 + 3' or 'exit' to quit): ")

    def check_operator(self, operator):
        if operator in const.VALID_OPERATORS:
            return True
        else:
            print("Invalid operator!")
            return False

    def get_operation(self, operator):
        operations = {
            '+': AddOperation(),
            '-': SubtractOperation(),
            '*': MultiplyOperation(),
            '/': DivideOperation(),
            '^': PowerOperation(),
            '√': SqrtOperation(),
            '%': ModulusOperation(),
        }
        return operations.get(operator)

    def calculate(self, num1, num2, operator):
        operation = self.get_operation(operator)
        if operation:
            return operation.calculate(num1, num2)
        else:
            print("Invalid operation.")
            return None

    def parse_expression(self, expression):
        try:
            expression = expression.replace(' ', '')
            if '√' in expression:
                num = float(expression[1:])
                return num, None, '√'
            for operator in const.VALID_OPERATORS:
                if operator in expression:
                    num1, num2 = expression.split(operator)
                    return float(num1), float(num2), operator
        except ValueError:
            raise ValueError("Invalid expression format")

    def display_history(self):
        if self.history:
            print("\n--- Calculation History ---")
            for record in self.history:
                print(record)
        else:
            print("No history available.")

    def perform_calculation(self):
        while True:
            user_input = self.get_input()

            if user_input.lower() == "history":
                self.display_history()
                continue
            elif user_input.lower() == "exit":
                break

            try:
                num1, num2, operator = self.parse_expression(user_input)

                if not self.check_operator(operator):
                    continue

                result = self.calculate(num1, num2, operator)

                if result is not None:
                    expression = f"{num1} {operator} {num2}" if operator != '√' else f"{operator}({num1})"
                    formatted_result = f"{expression} = {round(result, app_settings.decimal_places)}"
                    self.history.append(formatted_result)
                    self.log_to_file(expression, formatted_result)
                    print(formatted_result)

            except ValueError:
                print("Error: Invalid input.")
            except ZeroDivisionError as zde:
                print(zde)

            choice = input("Do you want to perform another calculation? (y/n): ")
            if choice.lower() != 'y':
                break
