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
        
math_object = MathOperations(4, 6)

print("Substract result: ", math_object.substract())
print(f"Substract result: {math_object.substract(4, 6)}")
print(f"Substract result: {math_object.substract("4", 6)}")