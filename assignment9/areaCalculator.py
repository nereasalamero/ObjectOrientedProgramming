import math

#Create a program (class AreaCalculator) that calculates the area of geometric shapes.
#The program should have “exception” classes: ShapeError as the base exception
#class, and two subclasses, NegativeDimensionError and InvalidShapeError.
#• ShapeError: Base exception class representing errors related to shape
#calculations.
#• NegativeDimensionError: Subclass of ShapeError, raised when the dimensions
#(length, width, etc.) provided to calculate the area are negative.
#• InvalidShapeError: Subclass of ShapeError, raised when an invalid shape type
#is provided for calculation.
#The program should include methods for calculating the area of rectangles and
#circles. Handle exceptions appropriately for negative dimensions and invalid shape
#types.
#AreaCalculator has class methods:
#• rectangle_area(self, length, width)
#• circle_area(self, radius)
#• calculate_area(self, shape_type, *args):

class ShapeError(Exception):
    pass

class NegativeDimensionError(ShapeError):
    def __init__(self, message="Negative dimensions are not allowed.", code=400):
        self.message = message
        self.code = code
        super().__init__(self.message)

class InvalidShapeError(ShapeError):
    def __init__(self, message="Invalid shape type."):
        self.message = message
        super().__init__(self.message)

class AreaCalculator:
    @staticmethod
    def rectangle_area(length, width):
        if length < 0 or width < 0:
            raise NegativeDimensionError("Dimensions must be non-negative.", 12)
        return length * width

    @staticmethod
    def circle_area(radius):
        if radius < 0:
            raise NegativeDimensionError("Radius must be non-negative.", 13)
        return math.pi * radius ** 2

    @staticmethod
    def calculate_area(shape_type, *args):
        if shape_type == "rectangle":
            if len(args) != 2:
                raise InvalidShapeError("Rectangle requires two dimensions (length, width).")
            return AreaCalculator.rectangle_area(args[0], args[1])
        elif shape_type == "circle":
            if len(args) != 1:
                raise InvalidShapeError("Circle requires one dimension (radius).")
            return AreaCalculator.circle_area(args[0])
        else:
            raise InvalidShapeError(f"Shape '{shape_type}' is not supported.")

# Example usage:
if __name__ == "__main__":
    try:
        area1 = AreaCalculator()
        rectangle_area = area1.calculate_area("rectangle", 5, 10)
    except NegativeDimensionError as e:
        print("Caught NegativeDimensionError:", e.message, e.code)
    except InvalidShapeError as e:
        print("Caught InvalidShapeError:", e)
    else:
        print("Rectangle area:", rectangle_area)

    try:
        area2 = AreaCalculator()
        circle_area = area2.calculate_area("circle", 7)
    except NegativeDimensionError as e:
        print("Caught NegativeDimensionError:", e.message, e.code)
    except InvalidShapeError as e:
        print("Caught InvalidShapeError:", e)
    else:
        print("Circle area:", circle_area)