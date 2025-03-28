# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         engine.py
# Description:  

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.size = 0

    def start(self):
        print(f"The engine starts {self.fuel_type} fuel.")
    
    def stop(self):
        print("The engine stops.")
    
    def engine_size(self, size: int):
        self.size = size

    def __eq__(self, value):
        if isinstance(value, Engine):
            return (self.fuel_type == value.fuel_type and self.size == value.size)
        return False

    def __lt__(self, value):
        if isinstance(value, Engine):
            return self.size < value.size
        return False
    
    def __call__(self, *args, **kwds):
        print(f"Instance of Engine called with args: {args} and kwargs: {kwds}")