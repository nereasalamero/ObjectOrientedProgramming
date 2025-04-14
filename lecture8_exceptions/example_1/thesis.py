from book import Book
from author import Author

class Thesis(Book):
    def __init__(self, name: str, author: str):
        self.name = name
        self.add_author(author)
        super().__init__(name, "code", 0)
        super().add_author(Author(author, 0))

    def add_author(self, author: str):
        self.author = author

    def summary(self):
        print(f"Thesis name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Number of authors: {len(self.authors)}")
        print("Authors names are from each book: ")
        for author in self.authors:
            print(f"['{author.name}']")