# Version 1.0.3
class Calculator:

    # def __init__(self, a, b): # Constructor
    #     pass

    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2



cal1 = Calculator()
print(cal1.add(12, 13))