# Author:       Nerea Salamero Labara
# Date:         29/01/2025
# File:         example_2.py
# Description:  Function to display object information.
#               Function to calculate the area of a rectangle.
#               Function to compare objects.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
def display_person_info(p: Person):
    print(f"Name: {p.name}, Age: {p.age}")

me = Person(name = "Humpty Dumpty", age = 1)
display_person_info(me)

brother = Person(name = "Little brother", age = 0.5)
display_person_info(brother)

class Person2:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def display_person_info(self, p):
        print(f"Name: {p.name}, Age: {p.age}")

me2 = Person2(name = "Humpty Dumpty", age = 1)
me2.display_person_info(me)

brother2 = Person2(name = "Little brother", age = 0.5)
brother2.display_person_info(brother)


# Function to calculate the area of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

def calculate_area(p):
    return p.length * p.width

r = Rectangle(20, 30)
area = calculate_area(r)
print(f"Area of the rectangle: {area}")


# Function to compare objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def compare(p1: Point, p2: Point):
    return p1.x == p2.x and p1.y == p2.y

p1 = Point(20, 31)
p2 = Point(20, 30)

if compare(p1, p2):
    print(f"Points are equal!")
else:
    print(f"Points are not equal!")

p1.x = 20
p1.y = 30

if compare(p1, p2):
    print(f"Points are equal!")
else:
    print(f"Points are not equal!")