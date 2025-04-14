# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         bookshelf.py
# Description:  
from book import Book
from bookContainer import BookContainer

class Bookshelf(BookContainer):
    def __init__(self):
        super().__init__()

    def add_book(self, book: Book, location: int):
        self.books.insert(location, book)