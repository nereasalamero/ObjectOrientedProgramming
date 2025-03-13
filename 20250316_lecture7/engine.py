
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print(f"The engine starts {self.fuel_type} fuel.")
    
    def stop(self):
        print("The engine stops.")
    
    def change_type(self, fuel_type):
        self.fuel_type = fuel_type