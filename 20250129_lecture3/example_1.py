
'''
# Simple class example
class Simple_class:
    pass
    
sc = Simple_class()
sc.name = "my first class"
sc.age = 1

print(sc.name)
print(sc.age)
print("...")

# Another example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog(name = "Nino", age = 12)
dog1.bark()

# Another example
class Cat:
    def __init__(self, name: str, age: int, times: int):
        self.name = name
        self.age = age
        self.times = times
    def miau(self):
        for i in range(self.times):
            print(f"{self.name} says Miau!")

cat1 = Cat(name = "Pipo", age = 5, times = 5)
cat1.miau()

# Another example
class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def miau(self, d, a=None, b=None, c=None):
        for i in range(d):
            if (a != None and b != None and c != None):
                print(f"{self.name} says Miau Loud {i}")
            if (a != None and b != None):
                print(f"{self.name} says Miau Normal {i}")
            if (a != None):
                print(f"{self.name} says Miau Silent {i}")
            else:
                print(f"{self.name} says Miau {i}")

cat = Cat(name = "Pipo", age = 5)
cat.miau(5)
cat.miau(5, 1)
cat.miau(5, 1, 1)
cat.miau(5, 1, 1, 1)
'''

# Another example - encapsulation
class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

dog2 = Dog(name = "Nino", age = 12)
dog2.bark()
dog2.celebrate_birthday()
dog2.celebrate_birthday()
dog2.celebrate_birthday()