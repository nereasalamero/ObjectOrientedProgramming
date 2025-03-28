# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         book.py
# Description:  
from author import Author

class Book:
    note = "This is a - book paperback"

    def __init__(self, name: str, code: str, price: int):
        self.name = name
        self.code = code
        self.price = price
        self.authors = []
        
    def add_author(self, author: Author):
        self.authors.append(author)

    def summary(self):
        names = []
        for author in self.authors:
            names.append(author.name)
        print("Book:", self.name)
        print("Authors:", len(self.authors))
        print("Author names from each book:", names)

    @classmethod
    def price(cls, name, code, price):
        return cls(name, code, price)
    
    @classmethod
    def hidden_information(cls):
        return cls.note
    
    @classmethod
    def copy_book(cls, old_book: "Book"):
        return cls(old_book.name, old_book.code, old_book.price)