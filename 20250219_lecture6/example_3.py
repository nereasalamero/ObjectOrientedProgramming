
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print(f"The engine starts {self.fuel_type} fuel.")
    
    def stop(self):
        print("The engine stops.")

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

my_engine = Engine("gasoline")
my_car = Car("Toyota", "Camry", my_engine)

my_car.start()
my_car.stop()
