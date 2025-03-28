# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         main.py
# Description:  
from borrowedbook import BorrowedBook
from book import Book
from member import Member
from author import Author
from library import Library

if __name__ == "__main__":
    #Create a list of members
    members = []
    members.append(Member("name 1", "1111", 23))
    members.append(Member("name 2", "2222", 56))
    members.append(Member("name 3", "3333", 12))
    members.append(Member("name 4", "4444", 2))

    itp = Book("Introduction to Programming", "qwerty", 50)

    read = []
    for member in members:
        read.append(BorrowedBook(member, itp, 30))

    #Print out the name of the member for each completed course
    for book in read:
        print(book.member.name)

    b = Book("The Catcher in the Rye", "asdfg", 10)
    b.add_author(Author("J.D. Salinger", 45))
    b.add_author(Author("Another author", 22))
    b.add_author(Author("Another author", 10))
    b.summary()

    b2 = Book("The Great Gatsby", "zxcvb", 15)
    b2.add_author(Author("F. Scott Fitzgerald", 45))
    b2.summary()

    l = Library()
    l.add_book(b)
    l.add_book(b2)

    for book in l.books:
        print("Book name: " + book.name)
        for author in book.authors:
            print("Author name: " + author.name)

    new_book = Book.price("The Great Gatsby", "zxcvb", 15)
    print(new_book.name)
    print(new_book.hidden_information())
    
    another_new_book = Book.copy_book(new_book)
    print(new_book)
    print(another_new_book)
