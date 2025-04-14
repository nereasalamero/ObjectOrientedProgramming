# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         main.py
# Description:  
from book import Book
from author import Author
from library import Library
from bookContainer import BookContainer
from bookshelf import Bookshelf
from thesis import Thesis

if __name__ == "__main__":
    b = Book("The Catcher in the Rye", "asdfg", 10)
    b.add_author(Author("J.D. Salinger", 45))
    b.add_author(Author("Another author", 22))
    b.add_author(Author("Another author", 10))

    b2 = Book("The Great Gatsby", "zxcvb", 15)
    b2.add_author(Author("F. Scott Fitzgerald", 45))

    container = BookContainer()
    container.add_book(b)
    container.add_book(b2)

    # Add the books (always to the beginning!)
    shelf = Bookshelf()
    shelf.add_book(b, 0)
    shelf.add_book(b2, 1)

    print("\n\nOur container: ")
    container.list_books()

    print("\n\nOur shelf: ")
    shelf.list_books()

    thesis = Thesis(name = "University of Arduino", author = "Savonia student")

    print(thesis.name)
    thesis.summary()