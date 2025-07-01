class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found book: {book}")
                return book
        print(f"Book '{title}' not found in the library.")
        return None
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{book}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found book: {book}")
                return book
        print(f"Book '{title}' not found in the library.")
        return None