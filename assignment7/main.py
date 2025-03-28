# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         main.py
# Description:  
from animal import Animal, Mammal, Bird

if __name__ == "__main__":
    mammal_instance = Mammal(name="Dog", age=3, sound="bark", fur_color="brown", num_legs=4)
    bird_instance = Bird(name="Eagle", age=5, sound="screech", feather_color="white", can_fly=True)

    mammal_instance.make_sound()
    mammal_instance.special_feature()

    bird_instance.make_sound()
    bird_instance.special_feature()