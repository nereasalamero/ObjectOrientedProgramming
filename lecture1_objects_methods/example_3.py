# Author:       Nerea Salamero Labara
# Date:         15/01/2025
# File:         example_3.py
# Description:  Objects and methods

# Built-in types
def my_func():
    print("Hello World!")

class MyClass:
    pass

obj = MyClass()
print(type(my_func))
print(type(obj))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person_obj = Person("John", 30)

print(type(person_obj))