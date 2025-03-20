# Author:       Nerea Salamero Labara
# Date:         15/01/2025
# File:         example_2.py
# Description:  Introduction to dictionaries.

# Creating a tuple
book_1 = {"name": "Little Women", "author": "Louisa May Alcott", "year": 1868}
book_2 = {"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}

print(book_1["name"])
print(book_2["name"])

book_2["name"] = "1984"

print(book_1["name"])
print(book_2["name"])