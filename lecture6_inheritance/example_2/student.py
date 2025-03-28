# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         student.py
# Description:  
from person import Person

class Student(Person):
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email