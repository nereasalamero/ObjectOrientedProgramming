# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         example_1.py
# Description:  

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    # Check if two engines are the same.
    def is_the_same_type(self, c1: "Car"):
        return self is c1
    
    def __eq__(self, value):
        if isinstance(value, Car):
            if  self.make == value.make and \
                self.model == value.model and \
                self.engine == value.engine:
                return True
            return False