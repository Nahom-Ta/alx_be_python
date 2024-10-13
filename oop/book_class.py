class Book:
    def __init__(self, title, author, year):
        """Initialize the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a string that recreates the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
