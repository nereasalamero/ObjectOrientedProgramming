# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         bookContainer.py
# Description:  
from book import Book

class BookContainer:
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        l = []
        for b in self.books:
            print(f"{b.name} :")
            for a in b.authors:
                l += [a.name]
            print(l)
            l.clear()


