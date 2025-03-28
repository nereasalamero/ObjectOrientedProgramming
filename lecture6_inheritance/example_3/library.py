# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         library.py
# Description:  
from book import Book

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        self.books.append(book)