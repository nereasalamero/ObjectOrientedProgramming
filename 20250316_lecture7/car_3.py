from random import randint, choice
from engine import Engine

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

def new_car():
    make = ["Toyota", "Ford", "Mitsubishi"]
    model = ["Camry", "F-150", "Outlander"]

    # random car name
    ma = choice(make)
    mo = choice(model)
    eng = Engine(str(randint(10000, 99999)))
    return Car(ma, mo, eng)

if __name__ == "__main__":
    cars = []

    cars.append(new_car())
    cars.append(new_car())
    cars.append(new_car())

    for car in cars:
        car.start()

    for car in cars:
        car.stop()