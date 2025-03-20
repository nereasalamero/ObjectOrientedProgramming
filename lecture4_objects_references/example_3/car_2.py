# Author:       Nerea Salamero Labara
# Date:         16/03/2025
# File:         car.py
# Description:  

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

# Main using a dictionary
if __name__ == "__main__":
    cars = {}

    my_first_engine = Engine("gasoline")
    my_second_engine = Engine("diesel")

    my_first_car = Car("Toyota", "Camry", my_first_engine)
    my_second_car = Car("Ford", "Escord", my_first_engine)
    my_third_car = Car("Honda", "Civic", my_second_engine)

    cars["k1"] = my_first_car
    cars["k2"] = my_second_car
    cars["k3"] = my_third_car

    my_first_car.make = "Toyota new"

    for car in cars:
        cars[car].start()
    
    for car in cars:
        cars[car].stop()

    
