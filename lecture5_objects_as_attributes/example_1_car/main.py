# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         main.py
# Description:  
from engine import Engine
from car_operator import Car

if __name__ == "__main__":
    my_first_engine = Engine("gasoline")
    my_second_engine = Engine("gasoline")

    my_first_car = Car("Mitsubishi", "Outlander", my_first_engine)
    my_second_car = Car("Mitsubishi", "Outlander", my_second_engine)

    print(my_first_car == my_second_car)

    my_first_engine.engine_size(size = 2)
    my_second_engine.engine_size(size = 3)

    print(my_first_engine < my_second_engine)
    print(my_second_engine < my_first_engine)

    print(my_first_car is my_first_car)
    print(my_first_car is my_second_car)

    # Calling the insance as if it was a function
    my_first_engine(1, 2, keyword_arg='example')
    my_first_engine(1, 2, 3, 4, arg='example')