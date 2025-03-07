import types

class Car:
    def __init__(self, make):
        self.make = make
        
def dynamic_method(self):
    print(f"This is a dynamic method for {self.make}")

my_car = Car("Toyota")  # Create an instance of the Car class
my_car.dynamic_method = types.MethodType(dynamic_method, my_car)    #Bind the dynamic method to the instance
my_car.dynamic_method()     # Call the dynamic method

class Car2:
    def __init__(self, make, model):
        self._make = make
        self._model = model
        self.make2 = make
        self.model2 = model
        
    def get_make(self):
        return self._make
    
    def set_make(self, make):
        if make:
            self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        if model:
            self._model = model
    
    def _protected_method(self):
        print("This is a protected method")
    
    def __private_method(self):
        print("This is a private method")
    
    def public_method(self):
        print("This is a public method")
        self._protected_method()
        self.__private_method()

car2 = Car2("Toyota", "Corolla")
car3 = Car2("Honda", "Civic")
print(car2.get_make())
print(car2.get_model())
print(car2.make2)
print(car2._model)

car2.set_make("Nissan")
car2.set_model("Sentra")
print(car2.get_make())
print(car2.get_model())

print(car3.get_make())
print(car3.get_model())

car2.public_method()
car2._protected_method()
#car2.__private_method() # This will raise an error
car2._Car2__private_method() # This will work
