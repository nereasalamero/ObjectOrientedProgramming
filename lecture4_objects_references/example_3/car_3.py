# Author:       Nerea Salamero Labara
# Date:         16/03/2025
# File:         car.py
# Description:  Objects within functions
 
from random import randint, choice
from engine import Engine

# Car class
class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine
    
    def start(self):
        print(f"The {self.make} {self.model} starts.")
        self.engine.start()

    def stop(self):        
        print(f"The {self.make} {self.model} stops.")
        self.engine.stop()

    # Check if two engines are the same.
    # Objects can act as arguments to methods.
    def is_the_same_type(self, e2: Engine):
        return self.engine is e2

    def is_the_same_car(self, c1: "Car"):
        return self is c1

# Function to create a new car
def new_car():
    make = ["Toyota", "Ford", "Mitsubishi"]
    model = ["Camry", "F-150", "Outlander"]

    # random car name
    ma = choice(make)
    mo = choice(model)
    eng = Engine(str(randint(10000, 99999)))
    return Car(ma, mo, eng)

def is_the_same_type(c1: Car, c2: Car):
    return c1 is c2

# Main 
if __name__ == "__main__":
    cars = []

    cars.append(new_car())
    cars.append(new_car())
    cars.append(new_car())

    for car in cars:
        car.start()

    for car in cars:
        car.stop()
    
    my_first_engine = Engine("gasoline")
    my_second_engine = Engine("diesel")

    my_first_car = Car("Toyota", "Camry", my_first_engine)
    my_second_car = Car("Ford", "Escord", my_first_engine)
    
    # Testing references
    print(my_first_car.is_the_same_type(my_second_car.engine))
    print(my_first_car.is_the_same_type(my_second_engine))

    print(is_the_same_type(my_first_car, my_second_car))

    print(my_first_car.is_the_same_car(my_first_car))
    print(my_first_car.is_the_same_car(my_second_car))

    print(my_first_car)
    print(my_second_car)
    print(str(my_first_car) == str(my_second_car))