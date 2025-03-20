# Author:       Nerea Salamero Labara
# Date:         12/02/2025
# File:         example_2.py
# Description:  Class definition for a math operations using helper and static methods.
 

class MathOperations:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def substract(self, x=None, y=None):
        if(x == None or y == None):
            return self.x - self.y
        elif(x != None and y != None):
            if self.is_number_ok(x,y) == True:
                return x - y
            else:
                return 0
    
    def is_number_ok(self, x, y):
        if isinstance(x, (int, float)) == True and isinstance(y, (int, float)) == True:
            return True
        else:
            return False
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y
        
math_object = MathOperations(4, 6)

print("Substract result: ", math_object.substract())
print(f"Substract result: {math_object.substract(4, 6)}")
print(f"Substract result: {math_object.substract("4", 6)}")
    
# Using static methods
result_add = MathOperations.add(3, 5)
result_multiply = MathOperations.multiply(4, 6)

print("Addition result: ", result_add)
print("Multiplication result: ", result_multiply)