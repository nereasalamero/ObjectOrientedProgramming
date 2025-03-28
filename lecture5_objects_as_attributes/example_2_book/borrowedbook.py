# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         borrowedbook.py
# Description:  
from book import Book
from member import Member

class BorrowedBook:
    def __init__(self, member: Member, book: Book, price: int):
        self.member = member
        self.book = book
        self.price = price