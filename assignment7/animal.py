# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         animal.py
# Description:  

class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes a {self.sound} sound.")

    def special_feature(self):
        pass


class Mammal(Animal):
    def __init__(self, name, age, sound, fur_color, num_legs):
        super().__init__(name, age, sound)
        self.fur_color = fur_color
        self.num_legs = num_legs

    def special_feature(self):
        print(f"{self.name} has {self.fur_color} fur and {self.num_legs} legs.")

class Bird(Animal):
    def __init__(self, name, age, sound, feather_color, can_fly):
        super().__init__(name, age, sound)
        self.feather_color = feather_color
        self.can_fly = can_fly

    def special_feature(self):
        print(f"{self.name} has {self.feather_color} feathers and can {'fly' if self.can_fly else 'not fly'}")