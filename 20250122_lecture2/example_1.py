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