# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         person.py
# Description:  

class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

    def change_email(self):
        self.email = self.email.replace(".com", ".fi")