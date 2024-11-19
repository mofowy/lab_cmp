class Operation:
    def calculate(self, num1, num2=None):
        raise NotImplementedError("This method should be overridden in subclasses")

class AddOperation(Operation):
    def calculate(self, num1, num2):
        return num1 + num2

class SubtractOperation(Operation):
    def calculate(self, num1, num2):
        return num1 - num2

class MultiplyOperation(Operation):
    def calculate(self, num1, num2):
        return num1 * num2

class DivideOperation(Operation):
    def calculate(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2

class PowerOperation(Operation):
    def calculate(self, num1, num2):
        return num1 ** num2

class SqrtOperation(Operation):
    def calculate(self, num1, num2=None):
        return num1 ** 0.5

class ModulusOperation(Operation):
    def calculate(self, num1, num2):
        return num1 % num2
