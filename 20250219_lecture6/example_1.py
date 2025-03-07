
class Car:
    def __init__(self, make):
        self.__make = make
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, make):
        if make:
            self.__make = make

my_car = Car("Toyota")
print(my_car.make)

my_car.make = "Honda"
print(my_car.make)
my_car.make = ""
print(my_car.make)