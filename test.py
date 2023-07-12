# Version 1.0.4
class Calculator:

    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2

    def pow(self, num1, num2):
        return num1**num2

    def sqrt(self, num):
        return num**(1/2)

cal1 = Calculator()
print(cal1.add(12, 13))
print(cal1.pow(12, 2))
print(cal1.sqrt(4))
