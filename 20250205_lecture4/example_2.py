from datetime import datetime, date
class Bird:
    species = "Unknown"

    def __init__(self, name, color, birthday, baby_birds = None):
        self.name = name
        self.color = color
        self.birthday = birthday
        self.baby_birds = baby_birds if baby_birds is not None else []
        pass

    def description(self):
        return f"{self.name} is a {self.color} bird and is born {self.birthday}."
    
    def make_sound(self, sound = "Chirp"):
        
        return f"{self.name} says {sound}"
    
    def change_attributes(self, new_name, new_color):
        self.name = new_name
        self.color = new_color

    def add_baby_bird(self, baby):
            self.baby_birds.append(baby)

    def change_species(self, new_species):
            Bird.species = new_species
    
    def age(self):
        calculated_age = datetime.now() - self.birthday
        return calculated_age
    
    def __str__(self):
        return f"{self.name} is a {self.color} bird and is born {self.birthday}."
    
    def __repr__(self):
        return f"{self.name} is a {self.color} bird and is born {self.birthday}."
    
bird1 = Bird(name = "Robin", color = "Red", birthday="2000-01-18")
bird2 = Bird(name = "Sparrow", color = "Brown", birthday="2024-01-16")

print(f"Bird name {bird1.name} is a {bird1.species}")
print(bird2.description())
print(bird1.make_sound())

# bird1.change_attributes(new_name="updated bird", new_color="grey")
# print(bird1.description())

# bird1.change_species("BAT")
# print(f"Bird name {bird1.name} is a {bird1.species}")

bird1.add_baby_bird(bird2)
print(f"{bird1.name}'s babies")
for baby in bird1.baby_birds:
    print(baby.description())

string = repr(bird1)
print(string)

string = str(bird1)
print(string)

