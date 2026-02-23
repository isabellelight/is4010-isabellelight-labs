"""
Lab 06 - Object-Oriented Programming
Defines Book and EBook classes with inheritance.
"""


class Book:
    """A class representing a physical book."""

    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book object.

        :param title: Title of the book
        :param author: Author of the book
        :param year: Publication year
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"\"{self.title}\" by {self.author} ({self.year})"

    def get_age(self):
        """Return the age of the book assuming current year is 2025."""
        current_year = 2025
        return current_year - self.year


class EBook(Book):
    """A class representing a digital book that inherits from Book."""

    def __init__(self, title: str, author: str, year: int, file_size: int):
        """
        Initialize an EBook object.

        :param title: Title of the book
        :param author: Author of the book
        :param year: Publication year
        :param file_size: File size in megabytes
        """
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation including file size."""
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"


if __name__ == "__main__":
    # Testing Book
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(book)
    print("Age:", book.get_age())

    # Testing EBook
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    print(ebook)
    print("Age:", ebook.get_age())