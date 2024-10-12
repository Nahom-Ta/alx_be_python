class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out
# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    # Method to check out a book
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Book was already checked out

    # Method to return a book
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Book was not checked out

    # Method to check if the book is available
    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    # Method to add a book to the library
    def add_book(self, book):
        self._books.append(book)

    # Method to check out a book by title
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
        print(f"Sorry, '{title}' is not available or doesn't exist.")

    # Method to return a book by title
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
        print(f"Sorry, '{title}' is either not checked out or doesn't exist.")

    # Method to list all available books
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
