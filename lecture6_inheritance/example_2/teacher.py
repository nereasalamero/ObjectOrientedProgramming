# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         teacher.py
# Description:  
from person import Person


class Teacher(Person):
    def __init__(self, name: str, address: str, email: str, room_number: int):
        self.name = name
        self.address = address
        self.email = email
        self.room_number = room_number